from django.shortcuts import render
from StudentManager.models import Students


from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User

import openpyxl

def importXl(request):
    #if bool(Group.objects.get(name="accounts") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="principal") in User.objects.get(username=request.user).groups.all() or
    #           Group.objects.get(name="administrator") in User.objects.get(username=request.user).groups.all()) == False:
    #    return render(request, 'dashboard/dashboardMain.html',
     #                 {'CheckStat': CheckStat.objects.get(id=1),
     #                  'students': Students.objects.all().filter(CheckedIn="Yes").order_by('LastName'),
      #                 'mode': 'viewCheckIn'})

    if "GET" == request.method:
        return render(request, 'importStudentLists.html', {})
    else:
        try:
            excel_file = request.FILES["excel_file"]

            # you may put validations here to check extension or file size

            wb = openpyxl.load_workbook(excel_file)

            # getting a particular sheet by name out of many sheets
            worksheet = wb["Sheet1"]
            print(worksheet)

            excel_data = list()
            # iterating over the rows and
            # getting value from each cell in row
            i = 0
            for row in worksheet.iter_rows():
                if i>0 and row[1].value is not None and row[2].value is not None:
                    row_data = list()
                    studentNames = str(row[2].value)
                    column2 = list()
                    column2 = studentNames.split(' ')
                    form_class = str(row[0].value)
                    LastName = str(row[1].value)
                    FirstName = ""
                    MiddleName = ""
                    Gender = str(row[3].value)
                    parentsEmail = str(row[4].value)
                    if len(column2) > 1:
                        FirstName = column2[0]

                    if len(column2) > 2:
                        MiddleName = column2[1]

                    if Students.objects.filter(LastName=LastName, FirstName=FirstName,
                                               MiddleName=MiddleName, ClassName=form_class).exists():
                            pass
                    else:
                        student = Students.objects.create(ClassName=form_class, LastName=LastName, FirstName=FirstName,
                                                      MiddleName=MiddleName, Gender=Gender, ParentEmail=parentsEmail)
                        student.save()
                        print(str(row[0].value) + str(row[1].value) + str(row[2].value))
                        for cell in row:
                            if i > 0:
                                row_data.append(str(cell.value))
                        excel_data.append(row_data)

                i += 1
            return "Upload Successfull!", excel_data
        except Exception as ex:
            return "Upload Failed!: " + str(ex), "None"