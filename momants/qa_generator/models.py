from django.db import models


class PageModel(models.Model):
    page_url = models.URLField()

    def save(self, *args, **kwargs):
        """
        On save, use DeepSeek to generate a list of questions.
        :param args:
        :param kwargs:
        :return:
        """

class QuestionModel(models.Model):
    page = models.ForeignKey(PageModel, on_delete=models.CASCADE)
    question_text = models.TextField()

    def save(self, *args, **kwargs):
        """
        On save, use DeepSeek to generate a list of answers.
        :param args:
        :param kwargs:
        :return:
        """

class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    answer_text = models.TextField()