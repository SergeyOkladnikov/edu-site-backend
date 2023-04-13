from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed

from quiz.models import *

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']

    def create(self, validated_data):
        question = get_object_or_404(Question, pk=self.context['view'].kwargs['question'])
        answer = Answer.objects.create(question=question, **validated_data)
        if answer.is_correct:
            question.correct_answers.add(answer)
        return answer

    def update(self, instance, validated_data):
        question = get_object_or_404(Question, pk=self.context['view'].kwargs['question'])
        instance.text = validated_data.get('text', instance.text)
        instance.is_correct = validated_data.get('is_correct', instance.is_correct)
        instance.save()
        if instance.is_correct:
            question.correct_answers.add(instance)
        else:
            question.correct_answers.remove(instance)

        return instance


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    correct_answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'score', 'answers', 'correct_answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        quiz = get_object_or_404(Quiz, pk=self.context['view'].kwargs['quiz'])
        question = Question.objects.create(quiz=quiz, **validated_data)
        for answer_data in answers_data:
            answer = Answer.objects.create(question=question, **answer_data)
            if answer.is_correct:
                question.correct_answers.add(answer)
        return question

    def update(self, instance, validated_data):
        answers_data = validated_data.get('answers', None)
        instance.text = validated_data.get('text', instance.text)
        # instance.quiz = get_object_or_404(Quiz, pk=self.context['view'].kwargs['quiz'])
        # instance.save()
        if answers_data:
            instance.correct_answers.clear()
            for item in Answer.objects.filter(question=instance):
                item.delete()
            for answer_data in answers_data:
                answer = Answer.objects.create(question=instance, **answer_data)
                if answer.is_correct:
                    instance.correct_answers.add(answer)

        instance.save()

        return instance


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'connection_code', 'is_published', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            answers_data = question_data.pop('answers')
            question = Question.objects.create(quiz=quiz, **question_data)
            for answer_data in answers_data:
                answer = Answer.objects.create(question=question, **answer_data)
                if answer.is_correct:
                    question.correct_answers.add(answer)
        return quiz

    def update(self, instance, validated_data):
        questions_data = validated_data.get('questions', None)
        instance.connection_code = validated_data.get('connection_code', instance.connection_code)
        instance.save()
        if questions_data:
            for item in Question.objects.filter(quiz=instance):
                item.delete()
            for question_data in questions_data:
                answers_data = question_data.pop('answers')
                question = Question.objects.create(quiz=instance, **question_data)
                for answer_data in answers_data:
                    answer = Answer.objects.create(question=question, **answer_data)
                    if answer.is_correct:
                        question.correct_answers.add(answer)
        return instance