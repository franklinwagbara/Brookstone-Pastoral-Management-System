from django.contrib import admin
from .models import Students, CheckIn, CheckOut, Seasons, CurrentSeason, Pointers

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('LastName', 'FirstName', 'MiddleName',
                    'Gender', 'DateOfBirth', 'ClassName', 'AcademicSession', 'DateOfAdmission')

class CheckInAdmin(admin.ModelAdmin):
    list_display = ('Student', 'Season', 'Passed',
                    'CheckedIn', 'DenyEntryCheckIn', 'PassCode', 'PC', 'Room', 'MetRequirements', 'DateTimeStamp', 'AccompanyGuardian', 'ByStaffPass', 'ByStaffCheckIn', 'DateTimeStampPC')

class PointersAdmin(admin.ModelAdmin):
    list_display = ('Season', 'PassCodePointer')

class SeasonsAdmin(admin.ModelAdmin):
    list_display = ('SeasonName', 'TotalStudents', 'TotalCheckIn', 'TotalNotCheckIn', 'TotalCheckOut', 'Date')
admin.site.register(Students, StudentsAdmin)
admin.site.register(CheckIn, CheckInAdmin)
admin.site.register(CheckOut)
admin.site.register(Seasons, SeasonsAdmin)
admin.site.register(CurrentSeason)
admin.site.register(Pointers, PointersAdmin)