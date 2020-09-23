from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import staffForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from smtplib import SMTPException
from django.urls import reverse
from django.contrib import messages
from StudentManager.models import Students
from .models import PrincipalInbox
from StudentManager.functions import FilterStudents
from StudentManager.forms import FilterStudentsForm
import concurrent.futures
import threading
from .functions import viewCheckInList
from django.contrib.auth.decorators import login_required
from StudentManager.models import Seasons, CurrentSeason, CheckIn
from Dashboard import decorators
from django.contrib.auth.models import Permission
from .decorators import admin

# Create your views here.
@login_required(login_url='login')
def homepage(request):
    season = Seasons.objects.get(SeasonName=CurrentSeason.objects.get(id=1).Season)
    return render(request, 'dashboard.html',
                  {'checkedins': CheckIn.objects.all().filter(Season=season).order_by('Student__LastName'),
                   'Season': Seasons.objects.get(SeasonName=CurrentSeason.objects.get(id=1).Season)})

#@user_passes_test(lambda u: Group.objects.get(name='administrator') in u.groups.all())
@login_required(login_url='login')
@admin
def sendStaffMail(request):
    if request.method == 'POST':
        #print("sendstaffmail" + str(Group.objects.get(id=1)))
        form = staffForm(request.POST)
        if form.is_valid():
            first_name = str(form.cleaned_data['FirstName'])
            last_name = str(form.cleaned_data['LastName'])
            email = str(form.cleaned_data['Email'])
            html_message = render_to_string('staffEmailForm.html', {
                'link': request.build_absolute_uri(reverse('users-register')), 'FirstName': first_name,
                'LastName': last_name, 'Email': email})
            plain_message = strip_tags(html_message)
            try:
                send_mail('Brookstone School Staff Registration',
                          plain_message,
                          'wagbarafranklin@yahoo.com',
                          ['wagbarafranklin@yahoo.com'],
                          html_message=html_message,
                          fail_silently=False)
                messages.success(request, "Email sent Successfully!")
            except SMTPException:
                messages.error(request, SMTPException)
            return render(request, 'FeedBack.html')
    else:
        form = staffForm()
    return render(request, 'registerStaff.html',
                  {'form': form})

def test(request):
    return render(request, "test.html")

