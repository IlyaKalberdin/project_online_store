from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from config.settings import EMAIL_HOST_USER
from users_app.forms import UserRegistrationForm, UserResetPasswordEnter, UserResetPasswordConfirm, UserResetPasswordUpdate
from users_app.models import User
from random import randint
from django import forms


class RegistrationView(CreateView):
    """
    Контроллер для регистрации пользователя
    """
    model = User
    form_class = UserRegistrationForm
    template_name = 'users_app/registration.html'
    success_url = reverse_lazy('users_app:login')
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save(commit=False)

        code = ''.join([str(randint(0, 9)) for i in range(6)])
        send_mail(
            'Подтверждение почты',
            f'Для подтверждения почты введи следующий код {code}',
            EMAIL_HOST_USER,
            [user.email]
        )

        self.request.session['code'] = code

        return redirect('users_app:confirm_email', user)


class ResetPasswordEnter(FormView):
    """
    Контроллер для запуска процесса сброса пароля, ввод почты
    """
    form_class = UserResetPasswordEnter
    template_name = 'users_app/reset_password_enter.html'
    extra_context = {'title': 'Ввод почты'}

    def form_valid(self, form):
        user_email = form.cleaned_data.get('user_email')

        code = ''.join([str(randint(0, 9)) for i in range(6)])
        send_mail(
            'Сброс пароля',
            f'Для подтверждения сброса пароля введи следующий код {code}',
            EMAIL_HOST_USER,
            [user_email]
        )

        self.request.session['code'] = code

        return redirect('users_app:reset_password_confirm', user_email)


class ResetPasswordConfirm(FormView):
    """
    Контроллер для подтверждения сброса пароля
    """
    form_class = UserResetPasswordConfirm
    template_name = 'users_app/reset_password_confirm.html'
    extra_context = {'title': 'Подтверждение сброса'}

    def form_valid(self, form):
        code1 = form.cleaned_data.get('code')
        code2 = self.request.session.get('code')
        user_email = self.kwargs.get('user_email')

        if code1 == code2:
            return redirect('users_app:reset_password_update', user_email)
        else:
            form.add_error('code', forms.ValidationError('Неверный код'))
            return super().form_invalid(form)


class ResetPasswordUpdate(UpdateView):
    """
    Контроллер для изменения пароля
    """
    model = User
    form_class = UserResetPasswordUpdate
    template_name = 'users_app/reset_password_update.html'
    extra_context = {'title': 'Изменение пароля'}
    success_url = reverse_lazy('users_app:login')

    def get_object(self, queryset=None):
        user_email = self.kwargs.get('user_email')
        obj = self.model.objects.get(email=user_email)
        return obj


def confirm_email(request, user_email):
    """
    Функция для подтверждения почты пользователя
    """
    user = User.objects.get(email=user_email)
    context = {'title': 'Подтверждение почты',
               'user_email': user}

    if request.method == 'POST':
        code1 = request.session.get('code')
        code2 = request.POST.get('code')

        if code1 == code2:
            user.is_confirmed_email = True
            user.save()
            return redirect('users_app:login')

    return render(request, 'users_app/confirm_email.html', context)
