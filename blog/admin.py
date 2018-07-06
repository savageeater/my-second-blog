from django.contrib import admin
from .models import Post
from blog.models import Post_board

# Register your models here.

admin.site.register(Post)
admin.site.register(Post_board)
