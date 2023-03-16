from django.urls import path
from .views.page_views import *

urlpatterns = [
    path('quizzes/<slug:connection_code>', index, name='home'),
    path('', page)
]