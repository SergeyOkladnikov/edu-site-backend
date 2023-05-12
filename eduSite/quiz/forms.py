from django import forms
from django.core.exceptions import ValidationError
from .models import Quiz


class QuizConnectionForm(forms.Form):
    connection_code = forms.SlugField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введи его сюда'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))

    def clean_connection_code(self):
        connection_code = self.cleaned_data['connection_code']
        if not Quiz.objects.filter(connection_code=connection_code).exists():
            raise ValidationError('Quiz с таким кодом присоединения не существует')
        return connection_code