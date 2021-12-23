from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        curr_user = request.user
        if not curr_user.is_faculty:
            messages.error(request, 'You do not have authorization to view Faculty Dashboard')
            return(redirect('login'))
        return(render(request, 'faculty/dashboard.html'))

# Create your views here.
