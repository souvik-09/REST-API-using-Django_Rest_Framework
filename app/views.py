from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from rest_framework import viewsets
from .models import Company, Employee
from .serailizers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    #companies/{company_id}/employees
    @action(detail=True, methods = ['GET'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employee = Employee.objects.filter(company=company)
            employees_serializer = EmployeeSerializer(employee, many=True, context={'request': request})
            return Response(employees_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                "Error": "Comapny doesn't exist!"
            })
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()   
    serializer_class = EmployeeSerializer     