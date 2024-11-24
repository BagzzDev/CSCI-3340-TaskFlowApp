from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

def home(request):
    return render(request, 'home.html')
    
def features(request):
    return render(request, 'features.html')

def about_us(request):
    return render(request, 'about_us.html')

def freqask(request):
    return render(request, 'frequently_asked.html')

def signup(request):
    return render(request, 'signup.html')

def log(request):
    return render(request, 'login.html')

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'task_form.html'

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'task_form.html'

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'task_confirm_delete.html'