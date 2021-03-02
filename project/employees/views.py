from django.shortcuts import render 
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializers

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers