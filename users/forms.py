from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    user_id = forms.CharField(label='아이디')
    name = forms.CharField(label='이름')
    class Meta:
        model = CustomUser
        fields = ('user_id', 'name', 'email', 'password1', 'password2')
        

class LoginForm(AuthenticationForm):
    user_id = forms.CharField(label='아이디')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'  # 실제 필드는 username이지만 라벨만 변경
        self.fields['username'].widget.attrs['placeholder'] = '아이디'