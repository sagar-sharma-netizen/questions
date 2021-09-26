from django.urls import path
from .views import list_questions

urlpatterns = [
    path('questions/', list_questions, name="list_questions")
    # path('')
]