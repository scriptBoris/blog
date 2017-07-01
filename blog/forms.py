from django import forms
from .models import Post
from .models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserBoxForm(forms.ModelForm):
    name = forms.CharField(label='логин', max_length=10)
    #password = forms.CharField(label='Password', max_length=10)
    password = forms.CharField(widget=forms.PasswordInput, label="пароль")
    class Meta:
        model = User
        fields = ('name', 'password',)
