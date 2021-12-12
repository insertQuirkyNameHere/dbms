from django import forms
from django.forms import fields
from django.http import request
from . import models
from spc.models import UpdateStudentDetails

class StudentDetailsForm(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = '__all__'
        
    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
        return student

class UpdateStudentDetailsForm(forms.ModelForm):
    class Meta:
        model = UpdateStudentDetails
        fields = '__all__'

    def save(self, commit=True):
        studentUpdateEntry = super().save(commit=False)
        if commit:
            studentUpdateEntry.save()
        return studentUpdateEntry