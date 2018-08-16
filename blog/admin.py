from django.contrib import admin
from .models import Post
from blog.models import Post_board

#from .models import SomeModel
# Register your models here.

admin.site.register(Post)
admin.site.register(Post_board)
