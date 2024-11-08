from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics

from college.models import Instructor, Student
from college.serializers import InstructorSerializer, StudentSerializer

class StudentsListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class InstructorListCreatView(generics.ListCreateAPIView):
    queryset= Instructor.objects.all()
    serializer_class=InstructorSerializer
        