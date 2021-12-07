from rest_framework import serializers
from accounts.models import CustomUser
from student.models import Student
from spc.models import UpdateStudentDetails, SpcDetails

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'is_active', 'is_staff', 'is_superuser', 'is_spc',
            'is_superSpc', 'is_placement', 'is_student', 'is_faculty')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'user', 'cgpa', 'backlogs', 'gap_years')

class UpdateStudentDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UpdateStudentDetails
        fields = ('id', 'name', 'user', 'cgpa', 'backlogs', 'gap_years')

class SpcDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpcDetails
        fields = ('id', 'student_id')
