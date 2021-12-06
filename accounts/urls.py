from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/student_user', views.RegisterStudent.as_view(), name = 'signupPage'),
    path('login/', views.LoginPage.as_view(), name='login')
]