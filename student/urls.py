from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='stu_dash'),
    path('createEntry/', views.CreateStudentEntry.as_view(), name='stu_detail_entry'),
    path('personalDetails/', views.PersonalDetails.as_view(), name='stu_personal_details'),
    path('editDetails/', views.UpdateStudentEntry.as_view(), name='stu_update_details'),
]