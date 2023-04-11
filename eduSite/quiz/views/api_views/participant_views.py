from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from quiz.serializers.participant_serializers import *

class AnswerPartialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerPartialSerializer


class QuestionPartialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionPartialSerializer


class QuizPartialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizPartialSerializer

    lookup_field = 'connection_code'


class QuizQuestionsIdListViewSet(mixins.RetrieveModelMixin,
                                 mixins.ListModelMixin,
                                 GenericViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizQuestionsIdListSerializer

class QuizQuestionsIdListConnectionCodeViewSet(QuizQuestionsIdListViewSet):
    lookup_field = 'connection_code'