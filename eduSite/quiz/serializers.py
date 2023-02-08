from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct', 'question']


class AnswerInQuestionSerializer(AnswerSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerInQuestionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'order', 'quiz', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)
        return question

    def update(self, instance, validated_data):
        answers_data = validated_data.get('answers', None)
        instance.text = validated_data.get('text', instance.text)
        instance.quiz = validated_data.get('quiz', instance.quiz)
        instance.save()
        if answers_data:
            for item in Answer.objects.filter(question=instance):
                item.delete()
            for answer_data in answers_data:
                Answer.objects.create(question=instance, **answer_data)
        return instance


class QuestionInQuizSerializer(QuestionSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'order', 'answers']


class QuestionBriefSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'order', 'quiz', 'answers']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionInQuizSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'connection_code', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            answers_data = question_data.pop('answers')
            question = Question.objects.create(quiz=quiz, **question_data)
            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)
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
                    Answer.objects.create(question=question, **answer_data)
        return instance


class QuizBriefSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'connection_code', 'questions']
