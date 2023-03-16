from django.shortcuts import render
from ..models import *


def index(request, connection_code):
    quiz = Quiz.objects.get(connection_code=connection_code)
    questions = Question.objects.filter(quiz=quiz)
    questions_w_answers = {}
    for q in questions:
        questions_w_answers[q] = Answer.objects.filter(question=q)
    context = {
        'title': 'Quiz',
        'connection_code': quiz.connection_code,
        'questions': questions_w_answers
    }
    return render(request, 'quiz/index.html', context=context)


def page(request):
    return render(request, 'quiz/page.html')