from django.shortcuts import render, redirect
from StudentManager.functions import viewStudents
from StudentManager.models import Students, Allowed, CurrentSeason, Seasons, CheckIn
import concurrent.futures
import threading
from django.utils import timezone
import datetime
from Manager.functions import incrementTotalCheckIn, decrementTotalCheckIn
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.urls import reverse
from .forms import PassCodeForm, DenyEntryForm, admitForm
from django.contrib.auth.decorators import login_required
from Manager.functions import incrementTotalCheckIn

@login_required(login_url='login')
def denyEntry(request, pk):
    if request.method == 'POST':
        form = DenyEntryForm(request.POST or None)
        if form.is_valid():
            _metRequirements = form.cleaned_data['MetRequirements']
            _denyEntry = form.cleaned_data['DenyEntryCheckIn']

            if _metRequirements == "No":
                if _denyEntry == "Yes":
                    _reasonCheckInPC = form.cleaned_data['ReasonCheckInPC']
                    
                    student = Students.objects.get(pk=pk)
                    currentSeason = CurrentSeason.objects.get(pk=1).Season
                    season = Seasons.objects.get(SeasonName=currentSeason)

                    checkIn = CheckIn.objects.get(Student=student, Season=season)

                    checkIn = CheckIn.objects.get(Student=student, Season=season)
                    checkIn.MetRequirements = _metRequirements
                    checkIn.DateTimeStampPC = timezone.now()
                    checkIn.CheckedIn = "No"
                    checkIn.DenyEntryCheckIn = _denyEntry
                    checkIn.ReasonCheckInPC = _reasonCheckInPC

                    checkIn.save()
                    messages.success(request, f'Student has being denied entry!')
            else:
                messages.error(request, "Operation Failed: Student can not be denied entry if they met the requirements!")
                form = DenyEntryForm()
    else:
        form = DenyEntryForm()
    return redirect("/CheckIn/viewCheckInProfile/" + str(pk))

@login_required(login_url='login')
def verifyPass(request):
    if request.method == 'POST':
        form = PassCodeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            pass_code = str(form.cleaned_data.get("PassCode"))

            print(pass_code)

            pass_code = pass_code.replace(" ", "")
            print(pass_code)
            season = CurrentSeason.objects.get(pk=1).Season

            if CheckIn.objects.filter(PassCode=pass_code, Season=season).exists():
                checkin = CheckIn.objects.get(PassCode=pass_code, Season=season)
                pk = checkin.Student.pk
                print(pk)
                messages.success(request, "Pass Code verification successfull!")
                return redirect("/CheckIn/viewCheckInProfile/" + str(pk))
            else:
                messages.error(request, "Invalid Pass Code!")

    else:
        form = PassCodeForm()
    return render(request, 'verifyPass.html', {'form': form})

@login_required(login_url='login')
def viewCheckInProfile(request, pk):
    student = Students.objects.get(pk=pk)
    season = CurrentSeason.objects.get(pk=1).Season
    checkin = ""
    allowed = ""
    if CheckIn.objects.filter(Student=student, Season=season).exists():
        checkedIn = "Yes"
        checkin = CheckIn.objects.get(Student=student, Season=season)
    else:
        checkedIn = "No"


    if Allowed.objects.filter(Student=student, Season=season).exists():
        allowed = Allowed.objects.get(Student=student, Season=season)
    else:
        allowed = ""

    form = PassCodeForm()
    if request.method == 'POST':
        form = PassCodeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            pass_code = str(form.clean_data["PassCode"])
            print(pass_code)
    else:
        form = PassCodeForm()

    return render(request, "checkInProfileCheckIn.html", {'student': student, 'checkedIn': checkedIn, 'checkin': checkin,
                                                   'allowed': allowed, 'form': form,
                                                    'form2': DenyEntryForm(request.POST or None),
                                                    'form3': admitForm(request.POST or None)})

def CheckIn_helper(request, id):
    if request.method == 'POST':
        form = admitForm(request.POST or None)
        if form.is_valid():
            _metRequirements = form.cleaned_data['MetRequirements']
            _pc = form.cleaned_data['PC']
            _room = form.cleaned_data['Room']
            _accompanyGuardian = form.cleaned_data['AccompanyGuardian']
            _accompanyGuardianPhone = form.cleaned_data['AccompanyGuardianPhone']
            _reasonCheckInPC = form.cleaned_data['ReasonCheckInPC']

            if _metRequirements == "Yes":
                student = Students.objects.get(pk=id)
                currentSeason = CurrentSeason.objects.get(pk=1).Season
                season = Seasons.objects.get(SeasonName=currentSeason)

                checkIn = CheckIn.objects.get(Student=student, Season=season)
                checkIn.MetRequirements = _metRequirements
                checkIn.PC = _pc
                checkIn.Room = _room
                checkIn.DateTimeStampPC = timezone.now()
                checkIn.CheckedIn = "Yes"
                checkIn.AccompanyGuardian = _accompanyGuardian
                checkIn.AccompanyGuardianPhone = _accompanyGuardianPhone
                checkIn.ReasonCheckInPC = _reasonCheckInPC
                checkIn.ByStaffCheckIn = (str(request.user.last_name) + ", " + str(request.user.first_name))

                checkIn.save()
                incrementTotalCheckIn()
                messages.success(request, f'Student has being checked-in successfully!')
            else:
                messages.error(request, f'Check-In Failed!: Student failed to meet the requirements.')

    return

def sendEMail(request, mailHead, recipient, template, context):
    msg=""
    if recipient != "None":
        html_message = render_to_string("" + template, {
            'context': context})
        plain_message = strip_tags(html_message)
        try:
            send_mail(mailHead,
                      plain_message,
                      'wagbarafranklin@yahoo.com',
                      [recipient],
                      html_message=html_message,
                      fail_silently=False)
            msg = "Email sent Successfully!"
            return msg
        except:
            msg = "Email failed!"
            return msg
    else:
        msg = "Operation Failed! No recipient provided."
    return msg

def wardCheckedInEmail(request, pk):
    student = Students.objects.get(pk=pk)
    mailHead = "You Ward have being Checked-in into Brookstone Secondary Boarding Facility"
    #recipient = student.ParentEmail
    recipient = "wagbarafranklin@yahoo.com"
    context = student
    template = "EmailPassSuccess.html"

    message = sendEMail(request, mailHead, recipient, template, context)

    return message

@login_required(login_url='login')
def Check_In(request, pk):
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    results = [executor.submit(checkin_helper, request, id), executor.submit(wardCheckedInEmail, request, id)]
    #    for f in concurrent.futures.as_completed(results):
    #        if f.result() != "EmailNoneResult":
    #           message = f.result()
    #           return message


    t1 = threading.Thread(target=CheckIn_helper, args=[request, pk])
    t2 = threading.Thread(target=wardCheckedInEmail, args=[request, pk])

    message = t1.start()
    message2 = t2.start()
    t1.join()
    return redirect("/CheckIn/viewCheckInProfile/" + str(pk))

    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return redirect("/Pass/viewCheckInProfile/" + str(pk))


#not in use yet
def dummyCheckIn(request, pk):
    print('here')
    if request.method == 'POST':
        form = PassCodeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            pass_code = str(form.clean_data["PassCode"])
            print(' nm ' + pass_code)

            return redirect("/CheckIn/viewCheckInProfile/" + str(pk))
    else:
        form = PassCodeForm()
    return render(request, 'dashboard/Students.html',
                  {'form': form, 'mode': 'AddStudent'})
