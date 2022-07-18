from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from NimapApp.models import MyNimapInfo,Clientinfo


class ClientInfoForm(forms.ModelForm):
    
    class Meta:
        model = MyNimapInfo
        fields = ("client_name","project","project_created","date",)

class ClientUserInfoForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")


