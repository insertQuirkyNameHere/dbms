from django import forms
from django.forms import widgets
from django.forms.widgets import PasswordInput
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password    = forms.CharField(required=True, widget=PasswordInput(attrs={'placeholder':'Password'}))

User = get_user_model()

class CreateStudentUserForm(forms.ModelForm):
    email       = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password    = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder' : 'Password'}))
    password2   = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model   = User
        fields  = ['email']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password is not None and password != password2:
            self.add_error("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        #user.is_student = False
        #user.is_spc = True
        if commit:
            user.save()
        return user

