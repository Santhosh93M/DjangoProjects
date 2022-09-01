from django.contrib import admin
from .models import Post


# Register your models here.


class PostBlog(admin.ModelAdmin):
    List_display = ('title', 'date_created', 'author')


admin.site.register(Post, PostBlog)
