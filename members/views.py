from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.forms import *
from django.contrib.auth.views import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class PasswordsChangeView(PasswordChangeView):
    form_class = EditPassForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user