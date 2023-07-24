from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from . models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name ='task'
    template_name = 'ToDo/task.html'

class TaskCreate(CreateView):
    model= Task
    fields = '__all__' 
    success_url =   reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    context_object_name = 'tasks'
    template_name = 'ToDo/tasks_form.html'