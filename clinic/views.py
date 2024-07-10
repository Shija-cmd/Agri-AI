#Importing important libraries
from django.shortcuts import render, redirect
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Farmer
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

#Login API
class CustomLoginView(LoginView):
    template_name = 'clinic/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
#register API    
class RegisterPage(FormView):
    template_name = 'clinic/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)         
# List of the task API
class TaskList(LoginRequiredMixin, ListView):
    model = Farmer
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user_name=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context
#Details for the task    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Farmer
    context_object_name = 'tasks'
    template_name = 'clinic/task.html'
#Creating tasks    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Farmer
    fields = '__all__'
    success_url = reverse_lazy('tasks')
#Updating tasks     
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Farmer
    fields = '__all__'
    success_url = reverse_lazy('tasks')
#Deleting tasks    
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Farmer
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
