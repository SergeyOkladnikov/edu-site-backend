from django.shortcuts import render, get_object_or_404
from ..models import *

def index(request):
    context = {
        'title': 'Quizzz'
    }

    return render(request, 'quiz/index.html', context=context)

def quiz_constructor(request):
    context = {
        'title': 'Создание Quiz'
    }

    return render(request, 'quiz/quiz-constructor.html', context=context)

def quiz_preview(request):
    context = {
        'title': 'Предпросмотр Quiz'
    }

    return render(request, 'quiz/quiz-preview.html', context=context)

def enter_name(request, connection_code):
    get_object_or_404(Quiz, connection_code=connection_code)
    return render(request, 'quiz/enter-name.html')

def quiz_solving(request, connection_code, name, question_number):
    quiz = get_object_or_404(Quiz, connection_code=connection_code)
    questions = quiz.questions.all()
    question = questions[question_number - 1]
    answers = question.answers.all()
    context = {
        'title': f'Quiz: {connection_code}',
        'name': name,
        'quiz': quiz,
        'question': question,
        'question_number': question_number,
        'questions_count': len(questions),
        'answers': answers
    }

    return render(request, 'quiz/quiz-solving.html', context=context)

def room(request, room_name):
    return render(request, 'quiz/results.html', {
        'title': f'Results: {Quiz.objects.get(pk=room_name).connection_code}',
        'room_name': room_name
    })