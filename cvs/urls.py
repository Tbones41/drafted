from django.urls import path
from . import views

urlpatterns = [
    path('cvs/', views.cvs, name='cvs')
]