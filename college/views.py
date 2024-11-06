from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from college.models import Student
from college.serializers import StudentSerializer

def students_list(request):
    students = Student.objects.first()
    serializer = StudentSerializer(students)
    return JsonResponse(serializer.data, safe=False)