from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics

from college.models import Student
from college.serializers import StudentSerializer

class StudentsListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer