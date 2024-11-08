from rest_framework import serializers

from college.models import Student
from college.models import Instructor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields = '__all__'