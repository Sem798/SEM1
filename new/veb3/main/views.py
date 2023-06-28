from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Sem
from .forms import TaskForm
from .forms import SemForm


def index(request):
    tasks =Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})

def about(request):

    sems = Sem.objects.all()
    return render(request, 'main/about.html', {'content': 'Страница про нас', 'sems': sems})

def DZ(request):
    return render(request, 'main/DZ.html')

def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html')

def DZ_1(request):
    form = SemForm()
    context = {
        'form': form
    }
    return render(request, 'main/DZ_1.html')
