from django import forms
from django.core.exceptions import ValidationError
from .models import Quiz, Answer, Question


class QuizConnectionForm(forms.Form):
    connection_code = forms.SlugField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введи его сюда',
            'form': 'quiz-connection'
        })
    )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введи имя сюда:',
            'form': 'quiz-connection'
        })
    )

    def clean_connection_code(self):
        connection_code = self.cleaned_data['connection_code']
        if not Quiz.objects.filter(connection_code=connection_code).exists():
            raise ValidationError('Quiz с таким кодом присоединения не существует')
        return connection_code


class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'name': 'answer-text',
                'class': 'new-question-text',
                'placeholder': 'Введите текст вопроса...'
            }),
        }

class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Answer
        fields = ['text', 'is_correct']
        widgets = {
            'text': forms.TextInput(attrs={
                'name': 'answer-text',
                'class': 'new-answer-text',
                'placeholder': 'Введите ответ...'
            }),
            'is_correct': forms.CheckboxInput()
        }
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['connection_code']
        widgets = {
            'connection_code': forms.TextInput(attrs={
                'id': 'create-quiz-code'
            })
        }

class DeleteQuestionForm(forms.Form):
    pass