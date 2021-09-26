from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings

from .models import QuestionModel


def list_questions(request):
    template_name = "question_list.html"
    query = request.GET.get('q')
    page = request.GET.get('page', 1)
    objects = QuestionModel.objects.all()
    if query:
        objects = objects.filter(
            Q(question_text__icontains=query)
            | Q(answer_text__icontains=query)
            # | Q(tags__contains=query)
        )
    paginated = Paginator(objects, per_page=settings.DEFAULT_PAGE_SIZE)
    page_obj = paginated.get_page(page)
    return render(request, template_name, {"page_obj": page_obj})

