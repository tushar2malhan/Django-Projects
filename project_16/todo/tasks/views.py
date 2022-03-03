from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={
        'tasks' : tasks,
        'form' : form,
    }
    return render(request,'tasks/list.html', context)

def updatetask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form' : form
    }

    return render(request, 'tasks/update_task.html', context)

def deletetask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {
        'item':item
    }
    return render(request, 'tasks/delete.html', context)