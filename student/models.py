from django.db import models
from django.contrib.auth import get_user_model

from department.models import Department

UserModel = get_user_model()
class Student(models.Model):
    name        = models.CharField(max_length=255, null=False)
    user        = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False)
    cgpa        = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    backlogs    = models.IntegerField(default=0, null=False)
    gap_years   = models.IntegerField(default=0, null=False)
    dept        = models.ForeignKey(Department, on_delete=models.CASCADE,  default=1)

    def __str__(self):
        return self.name

