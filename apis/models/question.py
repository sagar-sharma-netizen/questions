from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _

from .abstractmodel import AbstractModel


class QuestionModel(AbstractModel):
    """
    Question Model instance
    """
    question_text = models.TextField(
        verbose_name=_("Question text"),
        db_index=True,
        unique=True
    )
    answer_text = models.TextField(
        verbose_name=_("Answer text"),
        db_index=True,
        blank=True,
        default=""
    )
    tags = ArrayField(
        base_field=models.CharField(
            max_length=64,
        ),
        verbose_name="List of Tags",
        db_index=True,
        null=True,
        blank=True
    )

    class Meta:
        pass

    def __str__(self):
        return self.question_text
