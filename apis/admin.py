from django.contrib import admin
from django.conf import settings

from .models import QuestionModel

# Register your models here.


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "question_text",
        "answer_text"
    )
    search_fields = ("question_text", "answer_text", "tags")
    list_filter = ("is_active", "is_deleted")
    list_per_page = settings.DEFAULT_PAGE_SIZE
    readonly_fields = ()
    raw_id_fields = ()

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


# register
admin.site.register(QuestionModel, QuestionModelAdmin)
