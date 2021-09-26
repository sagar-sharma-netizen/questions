from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractModel(models.Model):
    """
    Abstract model class to provide some default columns to all models
    """
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now_add=True
    )
    is_deleted = models.BooleanField(
        verbose_name=_("Is deleted"),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_("Is active"),
        default=True
    )

    class Meta:
        # abstract model (only to be inherited)
        abstract = True

    def delete(self, force: bool = False):
        self.is_deleted = True
        if force:
            super().delete()
        self.save()
