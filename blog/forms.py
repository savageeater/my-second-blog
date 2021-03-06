from django import forms
from .models import Post
from blog.models import Post_board
from froala_editor.widgets import FroalaEditor


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)
        
class Post_board_Form(forms.ModelForm):
    class Meta:
        model = Post_board
        fields = ('title','text',)