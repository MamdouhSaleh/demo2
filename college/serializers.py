from rest_framework import serializers

from college.models import Student
from college.models import Instructor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['name']       

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields = '__all__'

class InstructorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['name']        