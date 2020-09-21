from django.contrib import admin
from StudentManager.models import Allowed

class AllowedAdmin(admin.ModelAdmin):
    list_display = ('Student', 'Season', 'Clear', 'DateTimeStamp')

admin.site.register(Allowed, AllowedAdmin)
