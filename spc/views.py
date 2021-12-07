from django.shortcuts import render
from django import views
# Create your views here.

class DashBoard(views.View):
    def get(self, request):
        curr_user = request.user
        return(render, 'spc/dashboard.html')

