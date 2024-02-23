from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import password_validation
from django import forms
from users_app.models import User
from django.utils.translation import gettext_lazy as _


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'number', 'country', 'avatar')


class UserResetPasswordEnter(forms.Form):
    user_email = forms.EmailField(label='Почта')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = 'Введите Вашу почту'

    def clean_user_email(self):
        cleaned_email = self.cleaned_data.get('user_email')

        if not User.objects.filter(email=cleaned_email):
            raise forms.ValidationError('Пользователь с такой почтой не найден')

        return cleaned_email


class UserResetPasswordConfirm(forms.Form):
    code = forms.CharField(label='Введите код направленный Вам на почту', max_length=6)


class UserResetPasswordUpdate(forms.ModelForm):
    password1 = forms.CharField(
        label='Введите новый пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user
