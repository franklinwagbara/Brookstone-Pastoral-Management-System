from django.shortcuts import render, redirect
from .forms import FilterStudentsForm, StudentsForm
from .models import Students, Allowed, CurrentSeason, Seasons
from .functions import viewStudents, updateStudentRecord, deleteStudentRecord
from django.contrib import messages
from Manager.functions import incrementTotalStudentsByOne
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Dashboard.decorators import admin, management, managerecords

@login_required(login_url='login')
@management
def ManageStudents(request):
    #if bool(Group.objects.get(name="accounts") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="principal") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="administrator") in User.objects.get(username=request.user).groups.all()) == False:
    #    return render(request, 'dashboard/dashboard.html',
    #                  {'CheckStat': CheckStat.objects.get(id=1),
    #                   'students': Students.objects.all().filter(CheckedOut="Yes").order_by('LastName') | Students.objects.all().filter(CheckedIn="Yes").order_by('LastName'),
    #                   'mode': 'viewCheckIn'})

    return viewStudents(request, "ManageStudents.html")
    #return render(request, "ManageStudents.html", {'students': Students.objects.all().filter().order_by('LastName'), 'form': FilterStudentsForm})

@login_required(login_url='login')
@managerecords
def viewUpdateStudentRecord(request, pk):
    return updateStudentRecord(request, pk, 'updateStudentRecord.html')

@login_required(login_url='login')
@managerecords
def viewDeleteStudentRecord(request, pk):
    return deleteStudentRecord(request, pk, "ManageStudents.html", FilterStudentsForm)

@login_required(login_url='login')
@managerecords
def viewAddStudent(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student added Successfully!')
            incrementTotalStudentsByOne()
            return redirect('StudentManager-viewAddStudent')
    else:
        form = StudentsForm()
    return render(request, 'viewAddStudent.html', {'form': form})

@login_required(login_url='login')
@management
def viewStudentProfile(request, pk):
    student = Students.objects.get(id=pk)
    return render(request, 'viewStudentProfile.html', {'student': student})

@login_required(login_url='login')
@management
def allowStudent(request, pk):
    #if bool(Group.objects.get(name="accounts") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="principal") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="administrator") in User.objects.get(username=request.user).groups.all()) == False:
    #    return render(request, 'dashboard/dashboard.html',
    #                  {'CheckStat': CheckStat.objects.get(id=1),
    #                   'students': Students.objects.all().filter(CheckedIn="Yes").order_by('LastName'),
    #                   'mode': 'viewCheckIn'})

    student = Students.objects.get(id=pk)
    season = Seasons.objects.get(SeasonName=CurrentSeason.objects.get(pk=1))
    if request.method == 'POST':
        if Allowed.objects.filter(Student=student, Season=season).exists():
            _allowed = Allowed.objects.get(Student=student, Season=season)
            if _allowed.Clear == "Yes":
                _allowed.Clear = "No"
                student.Clear = "No"
            else:
                _allowed.Clear = "Yes"
                student.Clear = "Yes"
            _allowed.save()
            student.save()
        else:
            Allowed.objects.create(Student=student, Season=season, Clear="Yes")
            student.Clear = "Yes"
            Allowed.save
            student.save()
        students = Students.objects.all()
        form = FilterStudentsForm()
        #return redirect('StudentManager-ManageStudents')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))