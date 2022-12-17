from django.urls import path
from . import views

urlpatterns = [
    path('interns/', views.interns, name='interns'),
    path('profile/', views.profile, name='profile')
]