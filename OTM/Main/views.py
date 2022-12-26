from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):

    tasks1 = Task.objects.all()
    return render(request, 'Main/main.html', {'title': 'main page', 'tasks': tasks1})


def about(request):
    return render(request, 'Main/about.html')


def contacts(request):
    return render(request, 'Main/contacts.html')


def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('main')

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'Main/tasks.html', context)
