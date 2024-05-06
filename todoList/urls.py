from django.urls import path
from todoList.views import create_task, update_task, delete_task, home

urlpatterns = [
    path("", home, name="home"),
    path("create_task/", create_task, name="create_task"),
    path("update_task/<int:pk>", update_task, name="update_task"),
    path("delete_task/<int:pk>", delete_task, name="delete_task"),
]