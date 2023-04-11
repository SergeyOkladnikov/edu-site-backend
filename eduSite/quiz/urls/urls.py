from django.urls import path, include
from rest_framework import routers

from quiz.urls.author_urls import author_router
from quiz.urls.participant_urls import participant_router
from quiz.views.page_views import *

urlpatterns = [
    path('', index, name='home'),
    path('quiz-constructor/', quiz_constructor, name='quiz_constructor'),
    path('quiz-preview/', quiz_preview, name='quiz_preview'),
    path('quiz-solving/', quiz_solving, name='quiz_solving'),
    path('api/participant/', include(participant_router.urls)),
    path('api/author/', include(author_router.urls)),
]