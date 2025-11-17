from django.shortcuts import render
from . models import Todolist

# Create your views here.
def index(request):
    todo_tasks = Todolist.objects.order_by('id')
    context = {'todo_tasks' : todo_tasks}
    return render(request, 'index.html', context)