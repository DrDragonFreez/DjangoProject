from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_email
from django.forms import PasswordInput, ModelForm
from .models import Comment


class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов")
    age = forms.IntegerField(label="Возраст клиента")
    basket = forms.BooleanField(label="Положить товар в корзину?")
    vyb = forms.NullBooleanField(label="Вы поедете в Сочи?")
    email = forms.EmailField(label="Электронный адрес")
    url_text = forms.URLField(label="Введите URL")
    file_path = forms.FilePathField(label="Выберите файл",
                                     path="C:/Users/danil/Desktop/Уник_РИНХ/3_курс/Web-технологии")
    file = forms.FileField(label="Файл")


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label='Пароль', widget=PasswordInput())


class RegisterForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

    username = forms.CharField(
        min_length=3, max_length=10, required=True, label='Никнейм',
        validators=[RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Может содержать только латинские буквы и цифры',
            code='invalid_username'
        )]
    )
    email = forms.CharField(min_length=3, required=True, label='Email')
    password = forms.CharField(widget=PasswordInput(), required=True, label='Пароль')
    password_confirm = forms.CharField(widget=PasswordInput(), required=True, label='Повторите пароль')

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError({
                'password_confirm': "Пароли не совпадают",
                'password': ""
            })

        username = cleaned_data.get("username")
        if username and get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError({'username': "Такой логин уже занят"})

        email = cleaned_data.get("email")
        if email:
            try:
                validate_email(email)
            except ValidationError:
                raise forms.ValidationError({'email': "Email не является валидным адресом"})

        return cleaned_data


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']