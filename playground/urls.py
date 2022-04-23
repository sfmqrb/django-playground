from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.say_hello, name='say_hello'),
]