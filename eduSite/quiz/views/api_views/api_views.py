from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from quiz.serializers.author_serializers import *
from quiz.serializers.participant_serializers import *
from quiz.serializers.serializers import *


# class QuizQuestionsIdListVewSet(mixins.RetrieveModelMixin,
#                                 mixins.ListModelMixin,
#                                 GenericViewSet):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizQuestionsIdListSerializer


# class QuizViewSet(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     # mixins.ListModelMixin,
#     GenericViewSet
# ):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer
#
#
# class QuestionViewSet(viewsets.ModelViewSet):
#     # queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#
#     def get_queryset(self):
#         quiz = self.kwargs['quiz']
#         quiz_instance = get_object_or_404(Quiz, pk=quiz)
#         return quiz_instance.questions.all()
#
#
# class AnswerViewSet(viewsets.ModelViewSet):
#     # queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#
#     def get_queryset(self):
#         quiz = self.kwargs['quiz']
#         question = self.kwargs['question']
#         get_object_or_404(Quiz, pk=quiz)
#         question_instance = get_object_or_404(Question, pk=question)
#         return question_instance.answers.all()


# class AnswerPartialViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerPartialSerializer
#
#
# class QuestionPartialViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionPartialSerializer
#
#
# class QuizPartialViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizPartialSerializer
#
#     lookup_field = 'connection_code'


class QuestionResultViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):
    queryset = QuestionResult.objects.all()
    serializer_class = QuestionResultSerializer


class QuizResultViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    # queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer
    def get_queryset(self):
        quiz = get_object_or_404(Quiz, connection_code=self.kwargs['connection_code'])
        return quiz.results.all()

