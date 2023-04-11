from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed

from quiz.models import *

class AnswerPartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'question']


class AnswerPartialNestedSerializer(AnswerPartialSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']


class QuestionPartialSerializer(serializers.ModelSerializer):
    answers = AnswerPartialNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'score', 'quiz', 'answers']


class QuestionPartialNestedSerializer(QuestionPartialSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'score', 'answers']


class QuizPartialSerializer(serializers.ModelSerializer):
    questions = QuestionPartialNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['connection_code', 'questions']


class QuizQuestionsIdListSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'connection_code', 'questions']