from django import forms
from django.forms import fields
from . import models

class StudentDetailsForm(forms.ModelForm):
    def __init__(self): 
        super(StudentDetailsForm, self).__init__()                       
        self.fields['user'].disabled = True

    class Meta:
        model = models.Student
        fields = ['name', 'user', 'cgpa', 'backlogs', 'gap_years']

    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
        return student