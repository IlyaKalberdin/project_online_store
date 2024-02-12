from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users_app.forms import UserRegistrationForm
from users_app.models import User


class RegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users_app/registration.html'
    success_url = reverse_lazy('users_app:login')

