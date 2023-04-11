from rest_framework import routers

from quiz.views.api_views.author_views import *

author_router = routers.SimpleRouter()

author_router.register(r'quizzes', QuizViewSet)
author_router.register(r'quiz/(?P<quiz>.+)/questions', QuestionViewSet, basename='Question')
author_router.register(r'quiz/(?P<quiz>.+)/question/(?P<question>.+)/answers', AnswerViewSet, basename='Answer')

