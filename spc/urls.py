from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.DashBoard.as_view(), name='spc_dash'),
    path('updateRequests/', views.UpdateRequests.as_view(), name='update_req'),
    path('personalDetails/', views.PersonalDetails.as_view(), name='spc_personal_details'),
    path('department/', views.StudentList.as_view(), name='stu_list')
]