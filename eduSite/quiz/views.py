from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework.views import APIView


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionBriefViewSet(QuestionViewSet):
    serializer_class = QuestionBriefSerializer


class QuizBriefViewSet(QuizViewSet):
    serializer_class = QuizBriefSerializer

