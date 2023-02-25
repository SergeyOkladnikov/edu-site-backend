from django.contrib import admin
from .models import *


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'connection_code')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'quiz')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question')


class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'participant', 'quiz')


class QuestionResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_correct', 'quiz_result')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
admin.site.register(QuestionResult, QuestionResultAdmin)
