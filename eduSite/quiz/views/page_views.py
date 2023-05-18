from django.forms import inlineformset_factory
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from .. import forms
from ..forms import QuizForm, DeleteQuestionForm, QuestionForm, AnswerForm
from ..models import *

def index(request):
    if request.method == 'POST':
        if 'quiz-connect' in request.POST:
            quiz_connection_form = forms.QuizConnectionForm(request.POST)
            quiz_creation_form = QuizForm()
            if quiz_connection_form.is_valid():
                try:
                    response = redirect(f'quiz-solving/{quiz_connection_form.cleaned_data["connection_code"]}/1')
                    response.set_cookie('name', quiz_connection_form.cleaned_data['name'])
                    return response
                except:
                    quiz_connection_form.add_error(None, 'Что-то пошло не так')
        if 'quiz-create' in request.POST:
            quiz_creation_form = QuizForm(request.POST)
            quiz_connection_form = forms.QuizConnectionForm()
            if quiz_creation_form.is_valid():
                try:
                    new_quiz = quiz_creation_form.save()
                    return redirect(f'/quiz/{new_quiz.pk}/1/')
                except:
                    quiz_creation_form.add_error(None, 'Ошибка создания Quiz')
    else:
        if 'name' in request.COOKIES.keys():
            quiz_connection_form = forms.QuizConnectionForm({'name': request.COOKIES['name']})
        else:
            quiz_connection_form = forms.QuizConnectionForm()
        quiz_creation_form = QuizForm()

    context = {
        'quiz_creation_form': quiz_creation_form,
        'quiz_connection_form': quiz_connection_form,
        'title': 'Quizzz'
    }

    return render(request, 'quiz/index.html', context=context)

def quiz_constructor(request, quiz_pk, question_order):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    questions = quiz.questions.all()
    questions_count = len(questions)
    del_question = DeleteQuestionForm()
    if question_order > questions_count + 1 or question_order <= 0:
        return HttpResponseNotFound()
    elif question_order <= questions_count:
        AnswerFormSet = inlineformset_factory(
            Question,
            Answer,
            form=AnswerForm,
            fields=['text', 'is_correct'],
            extra=1
        )
        if request.method == 'POST':
            print(request.POST)
            question = questions[question_order - 1]
            question_form = QuestionForm(request.POST, instance=question)
            answers_formset = AnswerFormSet(request.POST, instance=question)
            if question_form.is_valid():
                question_form.save()
            if answers_formset.is_valid():
                answers_formset.save()
            return redirect(f'/quiz/{quiz_pk}/{question_order}')

        question = questions[question_order - 1]
        question_form = QuestionForm(instance=question)
        answers_formset = AnswerFormSet(instance=question)
    else:
        AnswerFormSet = inlineformset_factory(
            Question,
            Answer,
            form=AnswerForm,
            fields=['text', 'is_correct'],
            extra=4
        )
        question = Question(quiz_id=quiz_pk)
        if request.method == 'POST':
            AnswerFormSet.extra = 0
            question_form = QuestionForm(request.POST, instance=question)
            answers_formset = AnswerFormSet(request.POST, instance=question)
            if question_form.is_valid():
                question = question_form.save()
            if answers_formset.is_valid():
                answers_formset.save()
            return redirect(f'/quiz/{quiz_pk}/{question_order + 1}/')
        question_form = QuestionForm(instance=question)
        answers_formset = AnswerFormSet(instance=question)

    context = {
        'question_form': question_form,
        'answers_formset': answers_formset,
        'del_question': del_question,
        'quiz_pk': quiz_pk,
        'questions_count': questions_count,
        'question_order': question_order,
        'prev': question_order - 1,
        'next': question_order + 1
    }
    return render(request, 'quiz/quiz-constructor.html', context=context)

def delete_question(request, quiz_pk, question_order):
    quiz = get_object_or_404(Quiz, pk=quiz_pk)
    questions = quiz.questions.all()
    questions_count = len(questions)
    if question_order > questions_count:
        return HttpResponseNotFound()
    if request.method == 'POST':
        questions[question_order - 1].delete()
        return redirect(f'/quiz/{quiz_pk}/{question_order}')

def quiz_preview(request):
    context = {
        'title': 'Предпросмотр Quiz'
    }

    return render(request, 'quiz/quiz-preview.html', context=context)



def quiz_solving(request, connection_code, question_number):
    quiz = get_object_or_404(Quiz, connection_code=connection_code)
    questions = quiz.questions.all()
    question = questions[question_number - 1]
    context = {
        'title': f'Quiz: {connection_code}',
        'name': request.COOKIES['name'],
        'quiz': quiz,
        'question': question,
        'question_number': question_number,
        'questions_count': len(questions),
        'answers': question.answers.all()
    }
    if len(question.answers.filter(is_correct=True)) == 1:
        return render(request, 'quiz/single-choice-solving.html', context=context)
    else:
        return render(request, 'quiz/multiple-choice-solving.html', context=context)
def room(request, room_name):
    return render(request, 'quiz/results.html', {
        'title': f'Results: {Quiz.objects.get(pk=room_name).connection_code}',
        'room_name': room_name
    })