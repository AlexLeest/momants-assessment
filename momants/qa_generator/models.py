from django.db import models


class PageModel(models.Model):
    page_url = models.URLField()

class QuestionModel(models.Model):
    page = models.ForeignKey(PageModel, on_delete=models.CASCADE)
    question_text = models.TextField()

class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    answer_text = models.TextField()