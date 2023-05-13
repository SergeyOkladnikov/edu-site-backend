from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from quiz.serializers.participant_serializers import *

class AnswerPartialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerPartialSerializer


class QuestionPartialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionPartialSerializer


class QuestionByOrderAPIView(
    APIView
):
    def get(self, request, connection_code, order):
        quiz = get_object_or_404(Quiz, connection_code=connection_code)
        questions = quiz.questions.all()
        if 1 <= order <= len(questions):
            question = questions[order - 1]
        else:
            return Response({'order': ['No question with this number']})
        serializer = QuestionPartialSerializer(question)
        return Response(serializer.data)


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