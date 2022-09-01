from . import views
from django.urls import path


urlpatterns = [
    path('title/<id>', views.BlogView, name='blog_view'),
    path('', views.HomeView, name='home_view'),
    path('about/', views.aboutview, name='about_view')
]