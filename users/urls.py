from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Additional paths for profile, login, logout, etc.
]
