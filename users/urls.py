from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile.as_view(), name='home'),
    path('userScramble/', views.UserScramble.as_view(), name='userScramble')
]