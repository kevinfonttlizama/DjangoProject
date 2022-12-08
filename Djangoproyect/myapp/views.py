from django.http import HttpResponse, JsonResponse
from .models import Proyect, Task
from django.shortcuts import render, redirect
from .forms import createNewTask, createNewProject

# Create your views here.


def index(request):
    title = 'Django course!!'
    return render(request, 'index.html', {
        'title': title
    })


def hello(request, username):
    return HttpResponse("<h2>Hello %s </h2>" % username)


def about(request):
    username = 'arthas'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    # projects = list(Proyect.objects.values())
    projects = Proyect.objects.all()
    return render(request, 'projects/proyects.html', {
        'proyects': projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create-task.html', {
            'form': createNewTask()
        })

    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], proyect_id=2)
        return redirect('tasks')


def create_Project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': createNewProject()

        })

    else:
        Proyect.objects.create(name=request.POST["name"])
        redirect('projects')