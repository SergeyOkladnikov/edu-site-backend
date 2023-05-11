from django.urls import path, include
from rest_framework import routers

from quiz.urls.author_urls import author_router
from quiz.urls.participant_urls import participant_router
from quiz.views.page_views import *

urlpatterns = [
    path('', index, name='home'),
    path('quiz-constructor/', quiz_constructor, name='quiz_constructor'),
    path('quiz-preview/', quiz_preview, name='quiz_preview'),
    path('api/participant/', include(participant_router.urls)),
    path('api/author/', include(author_router.urls)),

    path('quiz-solving/<slug:connection_code>/', enter_name, name='name'),
    path('quiz-solving/<slug:connection_code>/<str:name>/<int:question_number>/', quiz_solving, name='quiz'),
    path('quiz-results/<str:room_name>/', room, name='room'),
]
