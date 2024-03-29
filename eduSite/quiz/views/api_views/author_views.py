from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from quiz.serializers.author_serializers import *

class QuizViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    # mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    # queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz = self.kwargs['quiz']
        quiz_instance = get_object_or_404(Quiz, pk=quiz)
        return quiz_instance.questions.all()


class QuestionByOrderAPIView(
    APIView
):
    def get(self, request, quiz, order):
        quiz = get_object_or_404(Quiz, pk=quiz)
        questions = quiz.questions.all()
        if 1 <= order <= len(questions):
            question = questions[order - 1]
        else:
            return Response({'order': ['No question with this number']})
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

class AnswerViewSet(viewsets.ModelViewSet):
    # queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        quiz = self.kwargs['quiz']
        question = self.kwargs['question']
        get_object_or_404(Quiz, pk=quiz)
        question_instance = get_object_or_404(Question, pk=question)
        return question_instance.answers.all()