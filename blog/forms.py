from django import forms
from .models import Post
from .models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'text_full',)
