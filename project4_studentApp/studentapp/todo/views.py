from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Existing list & create view
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'todo/task_list.html', {
        'tasks': tasks,
        'form': form
    })

# Update view
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'todo/task_form.html', {
        'form': form,
        'task': task
    })

# Delete view
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {
        'task': task
    })