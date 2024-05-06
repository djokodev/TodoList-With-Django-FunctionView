from todoList.models import Task
from django.forms import ModelForm
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description', ]