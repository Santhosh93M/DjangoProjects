from django.shortcuts import render
from blog.models import Post
from django.views.generic import View
from .models import Post


# Create your views here.


def BlogView(request, id):
    objects = Post.objects.get(id=id)
    template_name = 'blog.html'
    return render(request, template_name, {'object': objects})


def HomeView(request):
    post = Post.objects.filter(status=1).order_by('date_created')
    template_name = 'Home.html'
    return render(request, template_name, {'post_list': post})


def aboutview(request):
    return render(request, 'about.html')