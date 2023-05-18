from django.contrib import admin
from .models import *

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'is_correct')

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'quiz')
    inlines = [AnswerInline]

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'connection_code')
    inlines = [QuestionInline]

class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'participant', 'quiz')


class QuestionResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_correct', 'quiz_result')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
admin.site.register(QuestionResult, QuestionResultAdmin)
