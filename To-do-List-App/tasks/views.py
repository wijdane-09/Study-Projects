from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'tasks/index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('home')

def task_complete(request, pk):
    # نسمحو غير POST لسلامة التغيير
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.completed = not task.completed  # toggle
        task.save()
    return redirect('home')

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('home')

def clear_completed(request):
    if request.method == 'POST':
        Task.objects.filter(completed=True).delete()
    return redirect('home')
