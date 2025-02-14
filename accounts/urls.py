from django.urls import  path
from . import views


urlpatterns=[
    path('', views.Register.as_view(), name='index'),
]