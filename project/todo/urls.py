from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = 'todo'
url_patterns = [
    path('todo/', TodoListAPIView.as_view(), name="todo_list"),
    path('todo/<int:pk>', TodoAPIView.as_view(), name="todo"),
    path('todo/reminder/<int:pk>', ReminderView.as_view(), name="todo_reminder"),
]


urlpatterns = format_suffix_patterns(url_patterns)
