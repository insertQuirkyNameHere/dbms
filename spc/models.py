from django.contrib.auth.backends import UserModel
from django.db import models
from django.contrib.auth import get_user_model
from student.models import Student

UserModel = get_user_model()
# Create your models here.
class UpdateStudentDetails(models.Model):
    name        = models.CharField(max_length=255, null=False)
    user        = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False)
    cgpa        = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    backlogs    = models.IntegerField(default=0, null=False)
    gap_years   = models.IntegerField(default=0, null=False)

class SpcDetails(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    