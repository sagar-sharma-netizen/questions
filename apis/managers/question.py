from django.db import models

from .abstract import AbstractManager, AbstractQueryset


class QuestionQueryset(AbstractQueryset):

    def filter_question_text(self, question_text):
        return self.filter(question_text=question_text)

    def filter_answer_text(self, answer_text):
        return self.filter(answer_text=answer_text)

    def filter_tags(self, tags):
        return self.filter(tags__in=tags)


class QuestionManager(AbstractManager):
    def get_queryset(self):
        return QuestionQueryset(self.model, using=self.db)
