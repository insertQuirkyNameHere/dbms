from django import views
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . import models
from . import forms
from spc.models import UpdateStudentDetails
from django.urls import reverse
# Create your views here.
class DashBoard(LoginRequiredMixin, View):
    def get(self, request):
        curr_user = request.user
        if not curr_user.is_student:
            messages.error(request, 'You do not have authorization to view Student Dashboard')
            return(redirect('login'))#redirect to user scramble instead

        curr_student = models.Student.objects.filter(user=curr_user)
        print(curr_student)
        context = dict()
        if curr_student is None:
            context['student'] = None
        else:
            context['student'] = curr_student
        #populate table with current values
        #Have link to edit values
        #Edit button should be disabled

        return (render(request, 'students/dashboard.html', context))

class CreateStudentEntry(LoginRequiredMixin, View):
    def get(self, request):
        curr_user = request.user
        curr_student = models.Student.objects.filter(user=curr_user)
        print(curr_student)
        if not curr_student:
            form = forms.StudentDetailsForm(initial={'user':curr_user})
            return render(request, 'students/dataEntry.html', {'form':form})
        else:
            messages.error(request, 'You have already entered your details. You cannot create a new entry!')
            return redirect(reverse('stu_dash'))

    def post(self, request):
        curr_user = request.user
        form = forms.StudentDetailsForm(request.POST)
        if form.is_valid:
            form.user = curr_user
            print(str(form.user))
            form.save()
        return(redirect(reverse('stu_dash')))

#Have to complete student update details
class UpdateStudentEntry(views.View):
    def get(self, request):
        curr_user = request.user
        curr_student = models.Student.objects.get(user=curr_user)
        curr_update_entry = UpdateStudentDetails.objects.filter(user=curr_user)
        print(curr_student)
        if not curr_update_entry:
            form = forms.StudentDetailsForm(initial={'user':curr_user})
            return render(request, 'students/dataEntry.html', {'form':form})
        else:
            messages.error(request, 'You have already entered your details. You cannot create a new entry!')
            return redirect(reverse('stu_dash'))
