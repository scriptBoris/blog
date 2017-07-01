from django import forms
from .models import Post
from .models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserBoxForm(forms.ModelForm):
    #login = forms.CharField(label='Login', max_length=10)
    #password = forms.CharField(label='Password', max_length=10)

    class Meta:
        model = User
        fields = ('name', 'password',)
