from django.shortcuts import redirect, render
from django.http import HttpResponseBadRequest
from django.views import View
from django.urls import reverse

class Profile(View):
    def get(self, request):
        return(render(request, 'users/profile.html'))

class UserScramble(View):
    def get(self, request):
        curr_user = request.user
        if curr_user.is_student:
            redirect(reverse('stu_dash'))
        elif curr_user.is_placement:
            redirect(reverse('placement_dash'))
        elif curr_user.is_faculty:
            redirect(reverse('faculty_dash'))
        elif curr_user.is_superSpc:
            redirect(reverse('superSpc_dash'))
