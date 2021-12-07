from django import views
from django.http import response
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse, reverse_lazy
from . import forms
from django.contrib import messages

UserModel = get_user_model()
# Create your views here.
class RegisterStudent(views.View):
    def get(self, request):
        form = forms.CreateStudentUserForm
        return render(request, 'registration/signup.html', {'form':form})

    def post(self, request):
        form = forms.CreateStudentUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            form.save()
        return(redirect('home'))

class LoginPage(views.View):
    def get(self, request):
        form = forms.LoginForm
        return render(request, 'registration/login.html', {'form': form})
    
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email   = form.cleaned_data['email']
            pwd     = form.cleaned_data['password']
            user = authenticate(username=email, password=pwd)
            print(str(user))
            if user is not None:
                login(request, user)
                print('reached')
                if user.is_student:
                    return(redirect(reverse('stu_dash')))
                if user.is_spc or user.is_superSpc:
                    return(redirect(reverse('stu_dash')))
                return(redirect(reverse('home')))
            else:
                if UserModel.objects.filter(email=email).exists():
                    messages.error(request, 'Incorrect username or password')
                else:
                    messages.error(request, 'This user does not exist. Please register')   
                return(render(request, 'registration/login.html', {'form':form}))
        else:
            messages.error(request, 'email did not pass validation')
            return(redirect('login'))
