from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Banner,UserInfo

class register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'username','class':'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder':'email','class':'form-input'}),
        }
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'repassword','class':'form-input'}))
           
class login(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username','class':'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-input'}))

class createBannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ('type','name','dis','img')
        widgets = {
            'type':forms.Select(),
            'name':forms.TextInput(),
            'dis':forms.Textarea(),
            'img':forms.FileInput()            
        }

