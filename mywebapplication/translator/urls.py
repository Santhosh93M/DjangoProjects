from . import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.translator_views, name='translator_view')
]