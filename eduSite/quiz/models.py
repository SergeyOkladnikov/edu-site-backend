from django.db import models


class Quiz(models.Model):
    connection_code = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return str(self.connection_code)


class Question(models.Model):
    text = models.CharField(max_length=300)
    order = models.IntegerField()
    quiz = models.ForeignKey('Quiz', related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
