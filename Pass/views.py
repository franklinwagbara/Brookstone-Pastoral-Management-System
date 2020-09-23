from django.shortcuts import render, redirect
from StudentManager.functions import viewStudents
from StudentManager.models import Students, Allowed, CurrentSeason, Seasons, CheckIn, Pointers
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
from django.contrib.auth.decorators import login_required
from Dashboard.decorators import management

@login_required(login_url='login')
def viewStudentsList(request):
    #if bool(Group.objects.get(name="accounts") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="principal") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="administrator") in User.objects.get(username=request.user).groups.all()) == False:
    #    return render(request, 'dashboard/dashboard.html',
    #                  {'CheckStat': CheckStat.objects.get(id=1),
    #                   'students': Students.objects.all().filter(CheckedOut="Yes").order_by('LastName') | Students.objects.all().filter(CheckedIn="Yes").order_by('LastName'),
    #                   'mode': 'viewCheckIn'})

    return viewStudents(request, "viewStudentsPass.html")

@login_required(login_url='login')
@management
def viewStudentsListAdmin(request):
    #if bool(Group.objects.get(name="accounts") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="principal") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="administrator") in User.objects.get(username=request.user).groups.all()) == False:
    #    return render(request, 'dashboard/dashboard.html',
    #                  {'CheckStat': CheckStat.objects.get(id=1),
    #                   'students': Students.objects.all().filter(CheckedOut="Yes").order_by('LastName') | Students.objects.all().filter(CheckedIn="Yes").order_by('LastName'),
    #                   'mode': 'viewCheckIn'})
    return viewStudents(request, "viewStudentsPassAdmin.html")

@login_required(login_url='login')
@management
def viewCheckInProfileAdmin(request, pk):
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

    return render(request, "checkInProfilePassAdmin.html", {'student': student, 'checkedIn': checkedIn, 'checkin': checkin,
                                                   'allowed': allowed})

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

    return render(request, "checkInProfilePass.html", {'student': student, 'checkedIn': checkedIn, 'checkin': checkin,
                                                   'allowed': allowed})

def Pass_helperAdmin(request, id):
    if request.method == "POST":
        reason = request.POST.getlist("reason")[0]
        current_season = CurrentSeason.objects.get(pk=1)
        season = Seasons.objects.get(SeasonName=current_season)
        student = Students.objects.get(pk=id)

        if Pointers.objects.filter(id=1).exists():
            pass_code = Pointers.objects.get(id=1).PassCodePointer + 1
            Pointers.objects.filter(id=1).update(PassCodePointer=pass_code)
            Pointers.save
        else:
            pass_code = CheckIn.objects.all().count() + 1
            Pointers.objects.create(id=1, Season=season, PassCodePointer=pass_code)
            Pointers.save

        pass_code = str(pass_code).zfill(4)
        print("here")
        if Allowed.objects.filter(Student=student, Season=season).exists():
            Allowed.objects.create(Student=student, Season=season, Clear="Yes")
            Allowed.save
        else:
            Allowed.objects.filter(Student=student, Season=season).update(Clear="Yes")
            Allowed.save

        if CheckIn.objects.filter(Student=student, Season=season).exists():
            CheckIn.objects.filter(Student=student,
                                   Season=season).update(Passed="Yes", PassCode=pass_code,
                                                         ReasonPass=reason, DateTimeStamp=timezone.now(),
                                                         ByStaffPass=(str(request.user.last_name) + ", " + str(request.user.first_name)))
            CheckIn.save
            #incrementTotalCheckIn()
        else:
            CheckIn.objects.create(Student=student,
                                   Season=season, Passed="Yes", PassCode=pass_code,
                                                         ReasonPass=reason,
                                                         DateTimeStamp=timezone.now(),
                                                         ByStaffPass=(str(request.user.last_name) + ", " + str(request.user.first_name)))
            CheckIn.save
            #incrementTotalCheckIn()

    print("checked in----")

def Pass_helper(request, id):
    if request.method == "POST":
        current_season = CurrentSeason.objects.get(pk=1)
        season = Seasons.objects.get(SeasonName=current_season)
        student = Students.objects.get(pk=id)

        if Pointers.objects.filter(id=1).exists():
            pass_code = Pointers.objects.get(id=1).PassCodePointer + 1
            Pointers.objects.filter(id=1).update(PassCodePointer=pass_code)
            Pointers.save()
        else:
            pass_code = CheckIn.objects.all().count() + 1
            Pointers.objects.create(id=1, Season=season, PassCodePointer=pass_code)
            Pointers.save

        pass_code = str(pass_code).zfill(4)
        if CheckIn.objects.filter(Student=student, Season=season).exists():
            CheckIn.objects.filter(Student=student,
                                   Season=season).update(Passed="Yes", PassCode=pass_code,
                                                         ReasonPass="Fulfilled all requirements.", DateTimeStamp=timezone.now(),
                                                         ByStaffPass=(str(request.user.last_name) + ", " + str(request.user.first_name)))
            CheckIn.save
            #incrementTotalCheckIn()
        else:
            CheckIn.objects.create(Student=student,
                                   Season=season, Passed="Yes", PassCode=pass_code,
                                                         ReasonPass="Fulfilled all requirements.",
                                                         DateTimeStamp=timezone.now(),
                                                         ByStaffPass=(str(request.user.last_name) + ", " + str(request.user.first_name)))
            CheckIn.save
            #incrementTotalCheckIn()

    print("checked in----")


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
def Pass(request, pk):
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    results = [executor.submit(checkin_helper, request, id), executor.submit(wardCheckedInEmail, request, id)]
    #    for f in concurrent.futures.as_completed(results):
    #        if f.result() != "EmailNoneResult":
    #           message = f.result()
    #           return message


    t1 = threading.Thread(target=Pass_helper, args=[request, pk])
    t2 = threading.Thread(target=wardCheckedInEmail, args=[request, pk])

    message = t1.start()
    message2 = t2.start()

    message = "Verification Successfull! Student is cleared to pass."
    if "Successfull" in message:
        messages.success(request, message)
    else:
        messages.error(request, message)

    return redirect("/Pass/viewCheckInProfile/" + str(pk))

    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return redirect("/Pass/viewCheckInProfile/" + str(pk))

@login_required(login_url='login')
@management
def PassAdmin(request, pk):
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #    results = [executor.submit(checkin_helper, request, id), executor.submit(wardCheckedInEmail, request, id)]
    #    for f in concurrent.futures.as_completed(results):
    #        if f.result() != "EmailNoneResult":
    #           message = f.result()
    #           return message

    t1 = threading.Thread(target=Pass_helperAdmin, args=[request, pk])
    t2 = threading.Thread(target=wardCheckedInEmail, args=[request, pk])

    message = t1.start()
    message2 = t2.start()

    message = "Verification Successfull! Student is cleared to pass."
    if "Successfull" in message:
        print("here " + message)
        messages.success(request, message)
    else:
        messages.error(request, message)

    return redirect("/Pass/viewCheckInProfileAdmin/" + str(pk))