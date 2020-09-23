from django.shortcuts import render
from django.http import HttpResponse
from .functions import importXl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User
from Dashboard.decorators import admin, managerecords


import openpyxl
from StudentManager.models import Students
from StudentManager.classes import CheckStat_class, Students_class

@login_required(login_url='login')
@managerecords
def importStudentLists(request):
    message = "None"
    excel_data = "None"
    message, excel_data = importXl(request)

    if "Failed" in message:
        messages.error(request, message)
    else:
        messages.success(request, message)

    return render(request, "importStudentLists.html", {"excel_data": excel_data})

@login_required(login_url='login')
@managerecords
def importTemplate(request):
    return render(request, "importStudentLists.html")

