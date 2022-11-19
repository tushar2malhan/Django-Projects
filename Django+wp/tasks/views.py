import os
import json
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from  django.shortcuts  import  render

@login_required(login_url='/')
def index(request):
    tasks = Task.objects.all().order_by('-id')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            if request.POST.get('title').lower().strip() == 'hello':
                post = request.POST.copy()
                post['title'] = 'goodbye'
                index(request)
            form.save()
        return redirect('/app')

    context={
        'tasks' : tasks,
        'form' : form,
    }
    return render(request,'tasks/list.html', context)

@login_required(login_url='/')
def updatetask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/app')

    context = {
        'form' : form
    }

    return render(request, 'tasks/update_task.html', context)

@login_required(login_url='/')
def deletetask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/app')

    context = {
        'item':item
    }
    return render(request, 'tasks/delete.html', context)


def  homepage(request):
    context = {
        'hostname': os.environ.get('HOSTNAME')}
    return render(request, 'tasks/home.html', context)