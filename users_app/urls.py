from django.contrib.auth.views import LoginView
from django.urls import path
from users_app.apps import UsersAppConfig

app_name = UsersAppConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    ]
