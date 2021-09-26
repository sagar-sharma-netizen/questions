from django.db import models


class AbstractQueryset(models.QuerySet):
    def filter_is_deleted(self, is_deleted: bool = False):
        return self.filter(is_deleted=is_deleted)

    def filter_is_active(self, is_active: bool = True):
        return self.filter(is_active=is_active)

    def delete(self, force: bool = False):
        self.update(is_deleted=True)
        if force:
            super().delete()


class AbstractManager(models.Manager):
    def get_queryset(self):
        return (
            super(AbstractManager, self)
            .get_queryset()
            .filter_is_deleted()
        )
