from StudentManager.models import Students
from django.utils import timezone

class CheckStat_class:
    def __init__(self):
        return

    def initialSetup(self):
        CheckStat.objects.create(TotalCkIn=0, TotalNotCkIn=0, NumberStudents=0, Student=1)
        CheckStat.save()

    def print(self):
        print(CheckStat.objects.all())
        for cs in CheckStat.objects.all():
            print(cs)
            print("{} {} {}".format(cs.pk, cs.TotalCkIn, cs.TotalNotCkIn))

    def insert(self, **kwargs):
        print("prior")
        print("before")
        print("here :" + str(Students.objects.get(pk=103)))
        print("after")
        expression = "CheckStat.objects.create("
        for key, value in kwargs.items():
            if key is "Student":
                print("Yes")
                student = Students.objects.get(pk=value)
                expression += key + "=" + str(student) + ","
            else:
                expression += key + "=" + str(value) + ","

        expression = expression[:-1]
        expression += ")"
        #expression = "CheckStat.objects.create(CheckInTime=timezone.now(), Student=Students.objects.get(pk=103), TotalCkIn=1, NumberStudents=Students.objects.all().count(),TotalNotCkIn=0)"
        print(expression)

        evl = eval(expression)
        print(str(evl))
        #CheckStat.save
        return "Insertion successfull!"

    def  setTotalStudentNumber(self):
        #CheckStat.objects.filter(pk=1).update(NumberStudents=Students.objects.all().count())
        #CheckStat.save
        return

    def print(self, **kwargs):
        row_data = ""
        for k in kwargs:
            row_data += str(kwargs[k]) + "   "
        row_data += '\n'
        #for cs in CheckStat.objects.all():
        #    for k in kwargs:
        #        if kwargs[k] is not None:
        #            val = eval("cs." + str(kwargs[k]))
        #            row_data += str(val) + "    " if val is not None else ""
        #    row_data += '\n'

        print(row_data)
        return row_data
class Students_class:
    def __init__(self):
        return

    def insert(self, **kwargs):
        expression = "Students.objects.create("
        for key, value in kwargs.items():
            expression += key + "='" + str(value) + "',"

        expression = expression[:-1]
        expression += ")"
        print(expression)

        print(eval(expression))
        Students.save
        return "Insertion successfull!"

    def print(self, **kwargs):
        row_data = ""
        for k in kwargs:
            row_data += str(kwargs[k]) + "   "
        row_data += '\n'
        for st in Students.objects.all():
            for k in kwargs:
                if kwargs[k] is not None:
                    val = eval("st." + str(kwargs[k]))
                    row_data += str(val) + "    " if val is not None else ""
            row_data += '\n'

        print(row_data)
        return row_data

    def delete(self, **kwargs):
        expression = "Students.objects.filter("
        for key, value in kwargs.items():
            expression += key + "='" + str(value) + "',"

        expression = expression[:-1]
        expression += ").delete()"
        print(expression)
        print(eval(expression))
        return "Deletion successfull"