from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('todo', views.TodoItemList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)