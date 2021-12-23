from django.shortcuts import render
from accounts.models import CustomUser
from student.models import Student
from spc.models import UpdateStudentDetails, SpcDetails
from rest_framework import viewsets

from .serializers import (CustomUserSerializer, StudentSerializer, UpdateStudentDetailsSerializer,
    SpcDetailsSerializer)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('email')
    serializer_class = CustomUserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer

class UpdateStudentDetailsViewSet(viewsets.ModelViewSet):
    queryset = UpdateStudentDetails.objects.all().order_by('name')
    serializer_class = UpdateStudentDetailsSerializer

class SpcDetailsViewSet(viewsets.ModelViewSet):
    queryset = SpcDetails.objects.all().order_by('id')
    serializer_class = SpcDetailsSerializer


