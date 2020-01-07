from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from .models import Record
import json

# Get from the user and store it on database

@api_view(["POST"])
def postDetails(request):
    try:
        details = json.loads(request.body)
        student_info = Record(name = details['name'], age = details['age'], dept = details['dept'])
        student_info.save()
        return JsonResponse("Added Successfully", safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
    

# Get the existing data from the database

@api_view(["GET"])
def fetchDetails(response):
    try:
        result = Record.objects.all()
        all_student = []
        for i in range(len(result)):
            one_data = {
                "name" : result[i].name,
                "age" : result[i].age,
                "dept": result[i].dept
            }
            all_student.append(one_data)
        return JsonResponse(all_student, safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)