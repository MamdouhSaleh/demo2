from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics

from college.models import Instructor, Student
from college.serializers import InstructorSerializer, InstructorUpdateSerializer, StudentSerializer, StudentUpdateSerializer

class StudentsListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class InstructorListCreatView(generics.ListCreateAPIView):
    queryset= Instructor.objects.all()
    serializer_class=InstructorSerializer
        
class InstructorDeleteView(generics.DestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JsonResponse("deleted instructor", safe=False)
    
class StudentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    partial = True

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse("Updated", safe=False)
    
class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return JsonResponse("deleted Student", safe=False)   
     
class InstructorUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorUpdateSerializer
    partial = True    