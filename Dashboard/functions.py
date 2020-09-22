from StudentManager.forms import FilterStudentsForm
from django.shortcuts import render, redirect
from StudentManager.models import Students, Allowed, Seasons, CheckIn, CurrentSeason

def viewCheckInList(request, template):
    if request.method == 'POST':
        form = FilterStudentsForm(request.POST)
        if form.is_valid():
            last_name = str(form.cleaned_data['LastName'])
            first_name = str(form.cleaned_data['FirstName'])
            class_name = str(form.cleaned_data['ClassName'])
            print(first_name + " + " + last_name + " + " + class_name)
            cs = CurrentSeason.objects.get(id=1)
            checkin = CheckIn.objects.all().filter(Student__FirstName__contains=first_name,
                                                                                  Student__LastName__contains=last_name,
                                                                                Student__ClassName__contains=class_name)
            print(checkin)
            for c in checkin:
                print(
                    str(c.Student.ClassName) + " + " + str(c.Season) + " + " + str(c.Passed) + " + " + str(c.CheckedIn))

            keys = {"Student__FirstName__icontains": first_name,
                    "Student__LastName__icontains": last_name,
                    "Student__ClassName__icontains": class_name}

            expression = "CheckIn.objects.all().filter("

            for key, value in keys.items():
                if str(value) != 'None':
                    expression += str(key) + "='" + value + "',"

            expression += "Season=cs.Season"

            expression += ").order_by('Student__LastName')"
            print(expression)
            checkedins = eval(expression)
            print(checkedins)
            return render(request, template, {'form': form, 'checkedins': checkedins})
    else:
        form = FilterStudentsForm()

    return render(request, template, {'form': form})

def viewCheckInList(request, template, Season):
    if request.method == 'POST':
        form = FilterStudentsForm(request.POST)
        if form.is_valid():
            last_name = str(form.cleaned_data['LastName'])
            first_name = str(form.cleaned_data['FirstName'])
            class_name = str(form.cleaned_data['ClassName'])
            print(first_name + " + " + last_name + " + " + class_name)
            cs = CurrentSeason.objects.get(id=1)
            checkin = CheckIn.objects.all().filter(Student__FirstName__contains=first_name,
                                                                                  Student__LastName__contains=last_name,
                                                                                Student__ClassName__contains=class_name)
            print(checkin)
            for c in checkin:
                print(
                    str(c.Student.ClassName) + " + " + str(c.Season) + " + " + str(c.Passed) + " + " + str(c.CheckedIn))

            keys = {"Student__FirstName__icontains": first_name,
                    "Student__LastName__icontains": last_name,
                    "Student__ClassName__icontains": class_name}

            expression = "CheckIn.objects.all().filter("

            for key, value in keys.items():
                if str(value) != 'None':
                    expression += str(key) + "='" + value + "',"

            expression += "Season=cs.Season"

            expression += ").order_by('Student__LastName')"
            print(expression)
            checkedins = eval(expression)
            print(checkedins)
            return render(request, template, {'form': form, 'checkedins': checkedins, 'Season': Season})
    else:
        form = FilterStudentsForm()

    return render(request, template, {'form': form, "Season": Season})
