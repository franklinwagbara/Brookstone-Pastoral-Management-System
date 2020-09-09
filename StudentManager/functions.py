from django.shortcuts import render, redirect, reverse
from .forms import FilterStudentsForm, StudentsForm
from .models import Students
from Manager.functions import decrementTotalStudentsByOne
from django.contrib import messages

def viewStudents(request, template):
    if request.method == 'POST':
        form = FilterStudentsForm(request.POST)
        if form.is_valid():
            last_name = str(form.cleaned_data['LastName'])
            first_name = str(form.cleaned_data['FirstName'])
            class_name = str(form.cleaned_data['ClassName'])

            keys = {"FirstName__icontains": first_name,
                    "LastName__icontains": last_name,
                    "ClassName__icontains": class_name}

            expression = "Students.objects.all().filter("

            for key, value in keys.items():
                if str(value) != 'None':
                    expression += str(key) + "='" + value + "',"

            if ',' in expression:
                expression = expression[:-1]

            expression += ").order_by('LastName')"
            students = eval(expression)
            return render(request, template, {'form': form, 'students': students})
    else:
        form = FilterStudentsForm()

    return render(request, template, {'form': form})

def updateStudentRecord(request, pk, template):
    #if bool(Group.objects.get(name="accounts") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="principal") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="administrator") in User.objects.get(username=request.user).groups.all()) == False:
    #    return render(request, 'dashboard/dashboardMain.html',
    #                  {'CheckStat': CheckStat.objects.get(id=1),
    #                   'students': Students.objects.all().filter(CheckedIn="Yes").order_by('LastName'),
    #                   'mode': 'viewCheckIn'})

    student = Students.objects.get(id=pk)
    form = StudentsForm(instance=student)
    if request.method == 'POST':
        form = StudentsForm(request.POST or None, request.FILES or None, instance=student)
        if form.is_valid():
            form.save()
            message = "Update was Successfull!"

            if "Successfull" in message:
                messages.success(request, message)
            else:
                messages.error(request, message)
            return render(request, template, {'form': form})
    else:
        form = StudentsForm(instance=student)
    return render(request, template, {'form': form, 'mode': 'AddStudent'})

def deleteStudentRecord(request, pk, template, form):
    #if bool(Group.objects.get(name="accounts") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="principal") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="administrator") in User.objects.get(username=request.user).groups.all()) == False:
    #    return render(request, 'dashboard/dashboardMain.html',
    #                  {'CheckStat': CheckStat.objects.get(id=1),
    #                   'students': Students.objects.all().filter(CheckedIn="Yes").order_by('LastName'),
    #                   'mode': 'viewCheckIn'})

    student = Students.objects.get(id=pk)
    print(str(student.pk))
    if request.method == 'POST':
        student.delete()
        message = decrementTotalStudentsByOne()

        if "Successfull" in message:
            messages.success(request, message)
        else:
            messages.error(request, message)

        return redirect('StudentManager-ManageStudents')