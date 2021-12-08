from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='spc_dash'),
]