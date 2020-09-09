from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    CheckinSeason = models.CharField(max_length=100, verbose_name="Check-In Season")
    SID = models.CharField(max_length=100, verbose_name="Student ID", null=True, blank=True)
    FirstName = models.CharField(max_length=100, verbose_name="First Name", null=True)
    MiddleName = models.CharField(max_length=100, verbose_name="Middle Name", null=True, blank=True)
    LastName = models.CharField(max_length=100, verbose_name="Last Name", null=True)
    gender = [('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')]
    Gender = models.CharField(max_length=100, choices=gender, null=True)
    DateOfBirth = models.DateField(verbose_name="Date of Birth", null=True, blank=True)
    ReasonForAllowing = models.CharField(max_length=100, blank=True, verbose_name="Reason for Allowing",
                                         default="Fulfilled all requirements.")
    width_field = 600
    height_field = 400
    photo = models.ImageField(upload_to="upload/%Y/%M/%D/", default="default.png", max_length=255, width_field="width_field",
                              height_field="height_field", verbose_name="Student's Passport")
    yeargroup = [
        ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')
    ]
    YearGroup = models.CharField(max_length=10, verbose_name="Year Group", null=True)

    classname = [
                 ('07B', '07B'), ('07S', '07S'), ('07I', '07I'), ('07P', '07P'), ('07R', '07R'),
                 ('08B', '08B'), ('08S', '08S'), ('08I', '08I'), ('08P', '08P'), ('08R', '08R'),
                 ('09B', '09B'), ('09S', '09S'), ('09I', '09I'), ('09P', '09P'),
                 ('10B', '10B'), ('10S', '10S'), ('10I', '10I'), ('10P', '10P'),
                 ('11B', '11B'), ('11S', '11S'), ('11I', '11I'), ('11P', '11P'),
                 ('12B', '12B'), ('12S', '12S'), ('12I', '12I'), ('12P', '12P'), ('IFY', 'IFY'),]
    ClassName = models.CharField(max_length=5, choices=classname, verbose_name="Class Name", null=True)

    term = [('Select', 'Select'), ('Autumn', 'Autumn'), ('Spring', 'Spring'), ('Summer', 'Summer')]
    Term = models.CharField(max_length=10, verbose_name="Term", null=True, choices=term, blank=True)
    AcademicSession = models.CharField(max_length=15, verbose_name="Academic Session", null=True, blank=True)
    DateOfAdmission = models.DateField(verbose_name="Date of Admission", null=True, blank=True)
    checked = [
        ('No', 'No'),
        ('Yes', 'Yes')
    ]
    Clear = models.CharField(max_length=3, verbose_name="Allow to check-in?", choices=checked, default="No")
    CheckedIn = models.CharField(max_length=3, verbose_name="Checked-In", choices=checked, default="No")
    CheckedOut = models.CharField(max_length=3, verbose_name="Checked-Out", choices=checked, default="No")
    Parent1 = models.CharField(max_length=50, verbose_name="Parent Name", null=True, blank=True)
    Parent2 = models.CharField(max_length=50, verbose_name="Other Name", null=True, blank=True)
    ParentEmail = models.EmailField(max_length=100, verbose_name="Parent Email", null=True, blank=True)

    Parent1Phone = models.CharField(max_length=15, verbose_name="Parent Phone", null=True, blank=True)
    Parent2Phone = models.CharField(max_length=15, verbose_name="Other Phone", null=True, blank=True)
    Parent1Address = models.CharField(max_length=255, verbose_name="Parent Address", null=True, blank=True)
    Parent2Address = models.CharField(max_length=255, verbose_name="Other Address", null=True, blank=True)
    ParentPhoto = models.ImageField(upload_to="upload/%Y/%M/%D/", default="default.png", max_length=255,
                              width_field="width_field",
                              height_field="height_field", verbose_name="Parent's Passport")
    OtherPhoto = models.ImageField(upload_to="upload/%Y/%M/%D/", default="default.png", max_length=255,
                              width_field="width_field",
                              height_field="height_field", verbose_name="Other's Passport")

    Parent1Temp = models.CharField(max_length=50, verbose_name="Parent Name", null=True, blank=True)
    Parent2Temp = models.CharField(max_length=50, verbose_name="Other Name", null=True, blank=True)
    ParentEmailTemp = models.EmailField(max_length=100, verbose_name="Parent Email", null=True, blank=True)

    Parent1PhoneTemp = models.CharField(max_length=15, verbose_name="Parent Phone", null=True, blank=True)
    Parent2PhoneTemp = models.CharField(max_length=15, verbose_name="Other Phone", null=True, blank=True)
    Parent1AddressTemp = models.CharField(max_length=255, verbose_name="Parent Address", null=True, blank=True)
    Parent2AddressTemp = models.CharField(max_length=255, verbose_name="Other Address", null=True, blank=True)
    ParentPhotoTemp = models.ImageField(upload_to="upload/%Y/%M/%D/", default="default.png", max_length=255,
                                    width_field="width_field",
                                    height_field="height_field", verbose_name="Parent's Passport")
    OtherPhotoTemp = models.ImageField(upload_to="upload/%Y/%M/%D/", default="default.png", max_length=255,
                                   width_field="width_field",
                                   height_field="height_field", verbose_name="Other's Passport")

    Alternative = models.BooleanField(max_length=5, verbose_name="Please allow my child to be checked-in by the person whose details are provided below.",
                                      default=False)
    Inbox_timestamp = models.DateTimeField(auto_now_add=True)

    Approved = models.BooleanField(max_length=5, verbose_name="Approved", default=False)

    CheckInTime = models.DateTimeField(null=True, blank=True)
    CheckedInBy = models.CharField(max_length=50, verbose_name="Checked-In by")

    CheckOutTime = models.DateTimeField(null=True, blank=True)
    CheckedOutBy = models.CharField(max_length=50, verbose_name="Checked-Out by")
    CheckOutSeason = models.CharField(max_length=50, verbose_name="Check-Out Season")
    class Meta:
        verbose_name = "Students"
        verbose_name_plural = "Students"

    def __str__(self):
         return self.LastName + ", " + self.FirstName

class Seasons(models.Model):
    SeasonName = models.CharField(max_length=100, verbose_name="Season Name", null=False, blank=True)
    Date = models.DateField(verbose_name="Date created", null=True, blank=True)
    TotalStudents = models.IntegerField(verbose_name="Total Number of Students", null=True, blank=True)
    TotalCheckIn = models.IntegerField(verbose_name="Total Number of Check-In", null=True, blank=True)
    TotalNotCheckIn = models.IntegerField(verbose_name="Total Number of Students not Checked-In", null=True, blank=True)
    TotalCheckOut = models.IntegerField(verbose_name="Total Number of Check Outs", null=True, blank=True)

    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Seasons"

    def __str__(self):
        return self.SeasonName

class CheckIn(models.Model):
    Student = models.ForeignKey(Students, on_delete=models.CASCADE)
    Season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    checked = [
        ('No', 'No'),
        ('Yes', 'Yes')
    ]
    checked3 = [
        ('Met Requirements?', 'Met Requirements?'),
        ('No', 'No'),
        ('Yes', 'Yes')
    ]
    checked4 = [
        ('Deny Entry?', 'Deny Entry?'),
        ('No', 'No'),
        ('Yes', 'Yes')
    ]
    Passed = models.CharField(max_length=3, verbose_name="Allowed to Pass the Gate?", choices=checked, default="No")
    CheckedIn = models.CharField(max_length=3, verbose_name="Checked into PC?", choices=checked, default="No")
    ReasonPass = models.CharField(max_length=200, verbose_name="Reason", default="")
    ReasonCheckInPC = models.CharField(max_length=200, verbose_name="Reason", null=True, blank=True)
    DenyEntryCheckIn = models.CharField(max_length=3, verbose_name="Deny Entry", choices=checked4, default="Deny Entry?")
    checked2 = [
        ('Choose Pastoral Centre', 'Choose Pastoral Centre'),
        ('Pastoral Center 1', 'Pastoral Center 1'),
        ('Pastoral Center 2', 'Pastoral Center 2'),
        ('Pastoral Center 3', 'Pastoral Center 3'),
        ('Pastoral Center 4', 'Pastoral Center 4'),
        ('Pastoral Center 5', 'Pastoral Center 5'),
        ('Pastoral Center 6', 'Pastoral Center 6')
    ]
    PC = models.CharField(max_length=20, verbose_name="Pastoral Center", choices=checked2, default="Choose Pastoral Centre")
    Room = models.CharField(max_length=3, verbose_name="Room Number", null=True, blank=True)
    Bed = models.CharField(max_length=3, verbose_name="Bed Number", null=True, blank=True)
    PassCode = models.CharField(max_length=5, verbose_name="Pass Code", null=True, blank=True)
    MetRequirements = models.CharField(max_length=3, verbose_name="Met Requirements?", choices=checked3, default="Met Requirements?")
    DateTimeStamp = models.DateTimeField(verbose_name="Pass Time", null=True, blank=True)
    AccompanyGuardian = models.CharField(verbose_name="Accompanying Guardian", max_length=50, null=True, blank=True)
    AccompanyGuardianPhone = models.CharField(max_length=15, verbose_name="Guardian Phone", null=True, blank=True)
    DateTimeStampPC = models.DateTimeField(verbose_name="Check-In Time", null=True, blank=True)
    ByStaff = models.CharField(max_length=60, verbose_name="Checked-In By", null=True, blank=True)
    Guardian1 = models.CharField(max_length=100, verbose_name="Guardian 1 Accompanying", null=True, blank=True)
    Guardian2 = models.CharField(max_length=100, verbose_name="Guardian 2 Accompanying", null=True, blank=True)
    Guardian1Phone = models.CharField(max_length=100, verbose_name="Guardian 1 Phone", null=True, blank=True)
    Guardian2Phone = models.CharField(max_length=100, verbose_name="Guardian 2 Phone", null=True, blank=True)


    class Meta:
        verbose_name = "Pass"
        verbose_name_plural = "CheckIns"

    def __str__(self):
        return self.Student.LastName + ", " + self.Student.FirstName + " " + self.Student.MiddleName

class CheckOut(models.Model):
    Student = models.ForeignKey(Students, on_delete=models.CASCADE)
    Season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    DateTimeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Check-Out Time")
    ByStaff = models.CharField(max_length=60, verbose_name="Checked-In By", null=True, blank=True)
    Guardian1 = models.CharField(max_length=100, verbose_name="Guardian 1 Accompanying", null=True, blank=True)
    Guardian2 = models.CharField(max_length=100, verbose_name="Guardian 2 Accompanying", null=True, blank=True)
    Guardian1Phone = models.CharField(max_length=100, verbose_name="Guardian 1 Phone", null=True, blank=True)
    Guardian2Phone = models.CharField(max_length=100, verbose_name="Guardian 2 Phone", null=True, blank=True)

    class Meta:
        verbose_name = "CheckOut"
        verbose_name_plural = "CheckOuts"

    def __str__(self):
        return self.Student

class CurrentSeason(models.Model):
    Season = models.ForeignKey(Seasons, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Current Season"

    def __str__(self):
        return str(self.Season)


class Allowed(models.Model):
    Student = models.ForeignKey(Students, on_delete=models.CASCADE)
    Season = models.ForeignKey(Seasons, on_delete=models.CASCADE, default=None)
    checked = [
        ('No', 'No'),
        ('Yes', 'Yes')
    ]
    Clear = models.CharField(max_length=3, verbose_name="Allow to check-in?", choices=checked, default="No")
    DateTimeStamp = models.DateTimeField(auto_now_add=True, verbose_name="Date")

    class Meta:
        verbose_name = "Allowed Students"

    def __str__(self):
        return str(self.Season)