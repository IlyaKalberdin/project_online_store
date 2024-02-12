from django.contrib.auth.views import LoginView, LogoutView
from users_app.views import RegistrationView
from django.urls import path
from users_app.apps import UsersAppConfig

app_name = UsersAppConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration')
    ]
