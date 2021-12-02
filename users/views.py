from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.views import View

class Profile(View):
    def get(self, request):
        return(render(request, 'users/profile.html'))
