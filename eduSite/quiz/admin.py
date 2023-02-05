from django.contrib import admin
from .models import *


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'connection_code')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_correct', 'question')
    list_editable = ('is_correct',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
