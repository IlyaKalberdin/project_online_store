from django.contrib.auth.views import LogoutView
from users_app.views import (RegistrationView, ResetPasswordEnter, ResetPasswordConfirm, ResetPasswordUpdate,
                             UserUpdateView, confirm_email, UserLoginView)
from django.urls import path
from users_app.apps import UsersAppConfig

app_name = UsersAppConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('registration/confirm_email/<user_email>', confirm_email, name='confirm_email'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
    path('reset_password_enter', ResetPasswordEnter.as_view(), name='reset_password_enter'),
    path('reset_password_confirm/<user_email>/', ResetPasswordConfirm.as_view(), name='reset_password_confirm'),
    path('reset_password_update/<user_email>/', ResetPasswordUpdate.as_view(), name='reset_password_update')
]
