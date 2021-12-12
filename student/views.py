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
        if not (curr_user.is_student):
            messages.error(request, 'You do not have authorization to view Student Dashboard!')
            return(redirect('userScramble'))#redirect to user scramble instead

        curr_student = models.Student.objects.filter(user=curr_user)
        print()
        context = dict()
        if not curr_student:
            context['student'] = None
        else:
            curr_student = models.Student.objects.get(user=curr_user)
            context['student'] = curr_student
        context['user'] = curr_user
        #populate table with current values
        #Have link to edit values
        #Edit button should be disabled

        return (render(request, 'students/dashboard.html', context))


class PersonalDetails(View):
    def get(self, request):
        curr_user = request.user
        if not (curr_user.is_student or curr_user.is_spc):
            messages.error(request, 'You do not have authorization to view Student Dashboard!')
            return(redirect('userScramble'))#redirect to user scramble instead

        curr_student = models.Student.objects.filter(user=curr_user)
        context = dict()
        if not curr_student:
            return redirect(reverse('stu_detail_entry'))
        else:
            curr_student = models.Student.objects.get(user=curr_user)
            context['student'] = curr_student
        context['user'] = curr_user
        return (render(request, 'students/personalDetails.html', context))

class CreateStudentEntry(LoginRequiredMixin, View):
    def get(self, request):
        curr_user = request.user
        curr_student = models.Student.objects.filter(user=curr_user)
        if not curr_student:
            form = forms.StudentDetailsForm(initial={'user':curr_user})
            form['user'].field.widget.attrs['hidden'] = True
            return render(request, 'students/dataEntry.html', {'form':form})
        else:
            messages.error(request, 'You have already entered your details. You cannot create a new entry!')
            return redirect(reverse('stu_dash'))

    def post(self, request):
        curr_user = request.user
        form = forms.StudentDetailsForm(request.POST)
        print(form)
        if form.is_valid:
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

            form = forms.UpdateStudentDetailsForm(
                initial={
                    'name' : curr_student.name,
                    'cgpa' : curr_student.cgpa,
                    'backlogs' : curr_student.backlogs,
                    'gap_years': curr_student.gap_years,
                    'dept' : curr_student.dept,
                }
            )
            form.initial['user'] = request.user
            form['user'].field.widget.attrs['hidden'] = True
            return render(request, 'students/dataEntry.html', {'form':form})
        else:
            messages.error(request, 'You have already requested an update. You cannot create a new one till action is taken on the current one!')
            return redirect(reverse('stu_dash'))

    def post(self, request):
        form = forms.UpdateStudentDetailsForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your request has been submitted for review')
        else:
            messages.error(request, 'Your request was no submitted as some field was invalid')

        return(redirect(reverse('stu_dash')))

