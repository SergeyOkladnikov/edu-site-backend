from django.contrib import admin
from .models import *


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'connection_code')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'quiz')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
