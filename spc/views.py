from django.contrib import messages
from django.shortcuts import redirect, render
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class DashBoard(LoginRequiredMixin, views.View):
    def get(self, request):
        curr_user = request.user
        if not curr_user.is_spc:
            messages.error(request, 'You do not have authorication to view SPC Dashboard!')
            return(redirect('login'))
        return(render(request, 'spc/dashboard.html'))

