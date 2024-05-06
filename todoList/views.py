from django.shortcuts import render, redirect
from todoList.forms import TaskForm
from todoList.models import Task
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    tasks = Task.objects.all()
    return render(request, "todoList/home.html", {"tasks":tasks})

def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")
        else:
            form = TaskForm()
    return render(request, "todoList/create_task.html", {"form":form})

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "todoList/update_task.html", {"form":form, "task":task})

def delete_task(request, pk):
    error = ""
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        if task.user != request.user:
            error = "Vous n'êtes pas autorisé à supprimer cette tâche."
        else:
            task.delete()
            return redirect("home")
    return render(request, "todoList/delete_task.html", {"task":task, "error":error})


