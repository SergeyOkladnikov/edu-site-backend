from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed

from quiz.models import *


# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = ['id', 'text', 'is_correct']
#
#     def create(self, validated_data):
#         question = get_object_or_404(Question, pk=self.context['view'].kwargs['question'])
#         answer = Answer.objects.create(question=question, **validated_data)
#         if answer.is_correct:
#             question.correct_answers.add(answer)
#         return answer
#
#     def update(self, instance, validated_data):
#         question = get_object_or_404(Question, pk=self.context['view'].kwargs['question'])
#         instance.text = validated_data.get('text', instance.text)
#         instance.is_correct = validated_data.get('is_correct', instance.is_correct)
#         instance.save()
#         if instance.is_correct:
#             question.correct_answers.add(instance)
#         else:
#             question.correct_answers.remove(instance)
#
#         return instance


# class AnswerNestedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = ['id', 'text', 'is_correct']


# class QuestionSerializer(serializers.ModelSerializer):
#     answers = AnswerSerializer(many=True)
#     correct_answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = Question
#         fields = ['id', 'text', 'score', 'answers', 'correct_answers']
#
#     def create(self, validated_data):
#         answers_data = validated_data.pop('answers')
#         quiz = get_object_or_404(Quiz, pk=self.context['view'].kwargs['quiz'])
#         question = Question.objects.create(quiz=quiz, **validated_data)
#         for answer_data in answers_data:
#             answer = Answer.objects.create(question=question, **answer_data)
#             if answer.is_correct:
#                 question.correct_answers.add(answer)
#         return question
#
#     def update(self, instance, validated_data):
#         answers_data = validated_data.get('answers', None)
#         instance.text = validated_data.get('text', instance.text)
#         # instance.quiz = get_object_or_404(Quiz, pk=self.context['view'].kwargs['quiz'])
#         # instance.save()
#         if answers_data:
#             instance.correct_answers.clear()
#             for item in Answer.objects.filter(question=instance):
#                 item.delete()
#             for answer_data in answers_data:
#                 answer = Answer.objects.create(question=instance, **answer_data)
#                 if answer.is_correct:
#                     instance.correct_answers.add(answer)
#
#         instance.save()
#
#         return instance


# class QuestionNestedSerializer(QuestionSerializer):
#     class Meta:
#         model = Question
#         fields = ['id', 'text', 'order', 'score', 'answers', 'correct_answers']


# class QuizQuestionsIdListSerializer(serializers.ModelSerializer):
#     questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = Quiz
#         fields = ['id', 'connection_code', 'questions']


# class QuizSerializer(serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True)
#
#     class Meta:
#         model = Quiz
#         fields = ['id', 'connection_code', 'questions']
#
#     def create(self, validated_data):
#         questions_data = validated_data.pop('questions')
#         quiz = Quiz.objects.create(**validated_data)
#         for question_data in questions_data:
#             answers_data = question_data.pop('answers')
#             question = Question.objects.create(quiz=quiz, **question_data)
#             for answer_data in answers_data:
#                 answer = Answer.objects.create(question=question, **answer_data)
#                 if answer.is_correct:
#                     question.correct_answers.add(answer)
#         return quiz
#
#     def update(self, instance, validated_data):
#         questions_data = validated_data.get('questions', None)
#         instance.connection_code = validated_data.get('connection_code', instance.connection_code)
#         instance.save()
#         if questions_data:
#             for item in Question.objects.filter(quiz=instance):
#                 item.delete()
#             for question_data in questions_data:
#                 answers_data = question_data.pop('answers')
#                 question = Question.objects.create(quiz=instance, **question_data)
#                 for answer_data in answers_data:
#                     answer = Answer.objects.create(question=question, **answer_data)
#                     if answer.is_correct:
#                         question.correct_answers.add(answer)
#         return instance


# class AnswerPartialSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = ['id', 'text', 'question']
#
#
# class AnswerPartialNestedSerializer(AnswerPartialSerializer):
#     class Meta:
#         model = Answer
#         fields = ['id', 'text']
#
#
# class QuestionPartialSerializer(serializers.ModelSerializer):
#     answers = AnswerPartialNestedSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Question
#         fields = ['id', 'text', 'score', 'quiz', 'answers']
#
#
# class QuestionPartialNestedSerializer(QuestionPartialSerializer):
#     class Meta:
#         model = Question
#         fields = ['id', 'text', 'score', 'answers']
#
#
# class QuizPartialSerializer(serializers.ModelSerializer):
#     questions = QuestionPartialNestedSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Quiz
#         fields = ['connection_code', 'questions']


# class QuestionResultCreationSerializer(serializers.Serializer):
#     chosen_answers = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all(), many=True)
#     is_correct = serializers.BooleanField(required=False)
#     question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
#     quiz_result = serializers.PrimaryKeyRelatedField(queryset=QuizResult.objects.all())
#
#     class Meta:
#         fields = ['id', 'chosen_answers', 'is_correct', 'question', 'quiz_result']
#
#     def create(self, validated_data):
#         question = validated_data.get('question', None)
#         chosen_answers = validated_data.pop('chosen_answers')
#         result = QuestionResult.objects.create(
#             is_correct=list(question.correct_answers.all()) == chosen_answers,
#             **validated_data
#         )
#         for answer in chosen_answers:
#             result.chosen_answers.add(answer)
#         return result

class QuestionResultSerializer(serializers.ModelSerializer):
    is_correct = serializers.BooleanField(required=False)

    class Meta:
        model = QuestionResult
        fields = ['id', 'chosen_answers', 'is_correct', 'question', 'quiz_result']

    def create(self, validated_data):
        question = validated_data.get('question', None)
        chosen_answers = validated_data.pop('chosen_answers')
        result = QuestionResult.objects.create(
            is_correct=list(question.correct_answers.all()) == chosen_answers,
            **validated_data
        )
        for answer in chosen_answers:
            result.chosen_answers.add(answer)
        return result


class QuizResultSerializer(serializers.ModelSerializer):
    question_results = QuestionResultSerializer(many=True, read_only=True)

    class Meta:
        model = QuizResult
        fields = ['id', 'participant', 'question_results']

    def create(self, validated_data):
        quiz = get_object_or_404(Quiz, connection_code=self.context['view'].kwargs['connection_code'])
        return QuizResult.objects.create(
            quiz=quiz,
            **validated_data
        )
