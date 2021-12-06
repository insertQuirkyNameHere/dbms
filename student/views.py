from django import views
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . import models
from . import forms
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

        return (render(request, 'student/dashboard.html'), context)

class StudentDetailsEntry(LoginRequiredMixin, View):
    def get(self, request):
        curr_user = request.user
        form = forms.StudentDetailsForm(initial={'user':curr_user})
        return render(request, 'students/dataEntry.html', {'form':form})