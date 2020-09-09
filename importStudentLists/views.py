from django.shortcuts import render
from django.http import HttpResponse
from .functions import importXl
from django.contrib import messages

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User


import openpyxl
from StudentManager.models import Students
from StudentManager.classes import CheckStat_class, Students_class

#####################

def test(request):
    Students.objects.all().delete()
    return HttpResponse(message)

######################
def importStudentLists(request):
    message = "None"
    excel_data = "None"
    message, excel_data = importXl(request)

    if "Failed" in message:
        messages.error(request, message)
    else:
        messages.success(request, message)

    return render(request, "importStudentLists.html", {"excel_data": excel_data})

def importTemplate(request):
    return render(request, "importStudentLists.html")

