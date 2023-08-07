from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView, FormView

from . models import Task, customProfile
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here

class CutomLogin(LoginView):
    template_name = 'ToDo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    

class RegisterPage(FormView):
    template_name = 'ToDo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self,  *args, **kwargs):
        if self.request.user.is_authenticated:

            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


    





class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] =  context['tasks'] .filter(user = self.request.user)
        context ['count'] = context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input    

        return context


class TaskDetail( LoginRequiredMixin, DetailView):
    model = Task
    context_object_name ='task'
    template_name = 'ToDo/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model= Task
    fields = ['title','description', 'complete']
    success_url =  reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate, self).form_valid(form)
        

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','description', 'complete']
    success_url = reverse_lazy('tasks')
    


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url=reverse_lazy('tasks')
    context_object_name = 'tasks'
    template_name = 'ToDo/tasks_form.html'

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = customProfile
    template_name = 'view_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        user_profile, created = customProfile.objects.get_or_create(user=self.request.user)
        return user_profile

# @login_required
# def view_profile(request):
#     return UserProfileDetailView.as_view()(request)


# class UserProfileCreateView(LoginRequiredMixin, CreateView):
#     model = customProfile
#     template_name = 'profile_create.html'
#     fields = ['profile']
#     success_url = reverse_lazy('tasks')  # Replace 'profile' with your profile URL name

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = customProfile
#     template_name = 'profile_form.html'
#     fields = ['profile']
#     success_url = reverse_lazy('tasks')  # Replace 'profile' with your profile URL name

#     def get_object(self, queryset=None):
#         # Override the get_object method to fetch the user's customProfile instance
#         # associated with the currently logged-in user.
#         return self.request.user.customprofile
