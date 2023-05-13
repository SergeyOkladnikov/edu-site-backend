from django.shortcuts import render, get_object_or_404, redirect
from .. import forms
from ..models import *

def index(request):
    if request.method == 'POST':
        quiz_connection_form = forms.QuizConnectionForm(request.POST)
        if quiz_connection_form.is_valid():
            response = redirect(f'quiz-solving/{quiz_connection_form.cleaned_data["connection_code"]}/1')
            response.set_cookie('name', quiz_connection_form.cleaned_data['name'])
            return response
        else:
            quiz_connection_form.add_error(None, 'Некорректные данные')
    else:
        if 'name' in request.COOKIES.keys():
            quiz_connection_form = forms.QuizConnectionForm({'name': request.COOKIES['name']})
        else:
            quiz_connection_form = forms.QuizConnectionForm()

    context = {
        'quiz_connection_form': quiz_connection_form,
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



def quiz_solving(request, connection_code, question_number):
    quiz = get_object_or_404(Quiz, connection_code=connection_code)
    questions = quiz.questions.all()
    question = questions[question_number - 1]
    answers = question.answers.all()
    context = {
        'title': f'Quiz: {connection_code}',
        'name': request.COOKIES['name'],
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