"""
URL configuration for demo2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from college.views import InstructorUpdateView, StudentsListCreateView, InstructorListCreatView, StudentUpdateView, StudentDeleteView,InstructorDeleteView 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentsListCreateView.as_view()),
    path('instructor/',InstructorListCreatView.as_view()),
    path('students/<int:pk>', StudentUpdateView.as_view()),
    path('students/<int:pk>/delete', StudentDeleteView.as_view()),
    path('instructor/<int:pk>/delete', InstructorDeleteView.as_view()),
    path('instructor/<int:pk>',InstructorUpdateView.as_view())

]