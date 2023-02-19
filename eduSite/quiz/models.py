from django.db import models


class Quiz(models.Model):
    connection_code = models.SlugField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return str(self.connection_code)


class Question(models.Model):
    text = models.CharField(max_length=300)
    order = models.IntegerField()
    score = models.IntegerField(default=1)
    correct_answers = models.ManyToManyField('Answer', related_name='correct_answers', blank=True)
    quiz = models.ForeignKey('Quiz', related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class QuizResult(models.Model):
    participant = models.CharField(max_length=100)
    quiz = models.ForeignKey('Quiz', related_name='results', on_delete=models.CASCADE)


class QuestionResult(models.Model):
    chosen_answers = models.ManyToManyField('Answer', related_name='chosen_answers', blank=True)
    is_correct = models.BooleanField()
    question = models.ForeignKey('Question', related_name='results', on_delete=models.CASCADE)
    quiz_result = models.ForeignKey('QuizResult', related_name='question_results', on_delete=models.CASCADE)
