from django.contrib import messages
from django.shortcuts import redirect, render
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UpdateStudentDetails
from student.models import Student
from department.models import Department
from django.urls import reverse
# Create your views here.

class DashBoard(LoginRequiredMixin, views.View):
    def get(self, request):
        curr_user = request.user
        if not curr_user.is_spc:
            messages.error(request, 'You do not have authorication to view SPC Dashboard!')
            return(redirect('userScramble'))
        context = dict()
        context['user'] = curr_user

        curr_spc = Student.objects.filter(user=curr_user)
        if not curr_spc:
            return redirect(reverse('stu_detail_entry'))
        else:
            curr_spc = Student.objects.get(user = curr_user)
            context['spc'] = curr_spc

        return(render(request, 'spc/dashboard.html', context))

class UpdateRequests(LoginRequiredMixin, views.View):
    def get(self, request):
        curr_user = request.user
        if not curr_user.is_spc:
            messages.error(request, 'You do not have authorization to view SPC Dashboard!')
            return(redirect('userScramble'))
        
        curr_spc = Student.objects.filter(user=curr_user)
        context = dict()
        context['user'] = curr_user
        if not curr_spc:
            return redirect(reverse('stu_detail_entry'))
        else:
            curr_spc = Student.objects.get(user = curr_user)
            updateReqSet = UpdateStudentDetails.objects.filter(dept = curr_spc.dept)
            context['spc'] = curr_spc
            context['updateReq'] = updateReqSet
            return render(request, 'spc/updateStudentEntry.html', context)
    
    def post(self, request):
        print(request.POST)
        if request.POST.get('accept'):
            received_name = request.POST.get('name')
            received_cgpa = request.POST.get('cgpa')
            received_backlogs = request.POST.get('backlogs')
            received_gap_years = request.POST.get('gap')
            received_dept = request.POST.get('dept')
            requested_student = Student.objects.get(user=request.POST.get('userId'))
            print(requested_student)
            requested_student.name = received_name
            requested_student.cgpa = received_cgpa
            requested_student.backlogs = received_backlogs
            requested_student.gap_years = received_gap_years
            requested_student.dept = Department.objects.get(id = received_dept)
            requested_student.save()

            requested_update_entry = UpdateStudentDetails.objects.get(user=request.POST.get('userId'))
            requested_update_entry.delete()
        else:
            requested_update_entry = UpdateStudentDetails.objects.get(user=request.POST.get('userId')).delete()
        return redirect(reverse('update_req'))
        
class PersonalDetails(LoginRequiredMixin, views.View):
    def get(self, request):
        curr_user = request.user
        if not curr_user.is_spc:
            messages.error(request, 'You do not have authorization to view SPC Dashboard!')
            return(redirect('userScramble'))

        curr_spc = Student.objects.filter(user=curr_user)
        context = dict()
        context['user'] = curr_user
        if not curr_spc:
            return redirect(reverse('stu_detail_entry'))
        else:
            curr_spc = Student.objects.get(user=curr_user)
            context['spc'] = curr_spc
            return render(request, 'spc/personalDetails.html', context)

class StudentList(LoginRequiredMixin, views.View):
    def get(self, request):
        curr_user = request.user
        if not curr_user.is_spc:
            messages.error(request, 'You do not have authorization to view SPC Dashboard!')
            return(redirect('userScramble'))

        curr_spc = Student.objects.filter(user=curr_user)
        context = dict()
        context['user'] = curr_user
        if not curr_spc:
            return redirect(reverse('stu_detail_entry'))
        else:
            curr_spc = Student.objects.get(user=curr_user)
            context['spc'] = curr_spc
            deptStudentList = Student.objects.filter(dept = curr_spc.dept)
            context['stu_list']  = deptStudentList
            return render(request, 'spc/studentList.html', context)

