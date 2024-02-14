from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users_app.forms import UserRegistrationForm
from users_app.models import User
from random import randint


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
        user = form.save()

        code = ''.join([str(randint(0, 9)) for i in range(6)])
        send_mail(
            'Подтверждение почты',
            f'Для подтверждения почты введи следующий код {code}',
            EMAIL_HOST_USER,
            [user.email]
        )

        self.request.session['code'] = code

        return redirect('users_app:confirm_email', user)


def confirm_email(request, user):
    """
    Функция для подтверждения почты пользователя
    """
    user = User.objects.get(email=user)
    context = {'title': 'Подтверждение почты',
               'user': user}

    if request.method == 'POST':
        code1 = request.session.get('code')
        code2 = request.POST.get('code')

        if code1 == code2:
            user.is_confirmed_email = True
            user.save()
            return redirect('users_app:login')

    return render(request, 'users_app/confirm_email.html', context)
