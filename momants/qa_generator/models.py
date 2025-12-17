from django.db import models


class Page(models.Model):
    page_url = models.URLField()

class Question(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    question_text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()