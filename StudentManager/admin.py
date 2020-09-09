from django.contrib import admin
from .models import Students, CheckIn, CheckOut, Allowed, Seasons, CurrentSeason

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('LastName', 'FirstName', 'MiddleName',
                    'Gender', 'DateOfBirth', 'ClassName', 'AcademicSession', 'DateOfAdmission')

class CheckInAdmin(admin.ModelAdmin):
    list_display = ('Student', 'Season', 'Passed',
                    'CheckedIn', 'DenyEntryCheckIn', 'PassCode', 'PC', 'Room', 'MetRequirements', 'DateTimeStamp', 'AccompanyGuardian', 'ByStaff', 'DateTimeStampPC')
admin.site.register(Students, StudentsAdmin)
admin.site.register(CheckIn, CheckInAdmin)
admin.site.register(CheckOut)
admin.site.register(Allowed)
admin.site.register(Seasons)
admin.site.register(CurrentSeason)