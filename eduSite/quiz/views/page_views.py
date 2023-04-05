from django.shortcuts import render

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

def quiz_solving(request):
    context = {
        'title': 'Quiz'
    }

    return render(request, 'quiz/quiz-solving.html', context=context)