"""eduSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quiz.views.api_views import *

participant_router = routers.SimpleRouter()
author_router = routers.SimpleRouter()

participant_router.register(r'quizzes', QuizPartialViewSet)
participant_router.register(r'questions', QuestionPartialViewSet)
participant_router.register(r'answers', AnswerPartialViewSet)
participant_router.register(r'quiz/(?P<connection_code>.+)/results', QuizResultViewSet, basename='QuizResult')
participant_router.register(r'result/(?P<result>.+)/question-results', QuestionResultViewSet)

author_router.register(r'quizzes', QuizViewSet)
author_router.register(r'quiz/(?P<quiz>.+)/questions', QuestionViewSet, basename='Question')
author_router.register(r'quiz/(?P<quiz>.+)/question/(?P<question>.+)/answers', AnswerViewSet, basename='Answer')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/participant/', include(participant_router.urls)),
    path('api/author/', include(author_router.urls)),
    path('', include('quiz.urls'))
]
