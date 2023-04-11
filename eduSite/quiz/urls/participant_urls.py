from rest_framework import routers
from quiz.views.api_views.api_views import *
from quiz.views.api_views.participant_views import *

participant_router = routers.SimpleRouter()

participant_router.register(r'quizzes', QuizPartialViewSet)
participant_router.register(r'questions', QuestionPartialViewSet)
participant_router.register(r'answers', AnswerPartialViewSet)
participant_router.register(r'quiz/(?P<connection_code>.+)/results', QuizResultViewSet, basename='QuizResult')
participant_router.register(r'result/(?P<result>.+)/question-results', QuestionResultViewSet)

participant_router.register(r'quiz/question-ids/connection_code', QuizQuestionsIdListConnectionCodeViewSet)
participant_router.register(r'quiz/question-ids/id', QuizQuestionsIdListViewSet)