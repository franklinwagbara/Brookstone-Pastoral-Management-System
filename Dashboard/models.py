from django.db import models
from StudentManager.models import Students

class PrincipalInbox(models.Model):
    student = models.ForeignKey(Students, verbose_name="Student", on_delete=models.CASCADE)
    viewed = models.CharField(max_length=4, verbose_name="Viewed", null=True, blank=True)
    approved = models.CharField(max_length=4, verbose_name="Approved", null=True, blank=True)