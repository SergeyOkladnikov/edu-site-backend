from django.urls import path
from .views.page_views import *

urlpatterns = [
    path('', index, name='home'),
    path('quiz-constructor/', quiz_constructor, name='quiz_constructor'),
    path('quiz-preview/', quiz_preview, name='quiz_preview'),
    path('quiz-solving/', quiz_solving, name='quiz_solving')
]