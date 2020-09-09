# Generated by Django 2.2.6 on 2020-08-16 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SeasonName', models.CharField(blank=True, max_length=100, verbose_name='Season Name')),
                ('Date', models.DateField(blank=True, null=True, verbose_name='Date created')),
                ('TotalStudents', models.IntegerField(blank=True, null=True, verbose_name='Total Number of Students')),
                ('TotalCheckIn', models.IntegerField(blank=True, null=True, verbose_name='Total Number of Check-In')),
                ('TotalNotCheckIn', models.IntegerField(blank=True, null=True, verbose_name='Total Number of Students not Checked-In')),
                ('TotalCheckOut', models.IntegerField(blank=True, null=True, verbose_name='Total Number of Check Outs')),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckinSeason', models.CharField(max_length=100, verbose_name='Check-In Season')),
                ('SID', models.CharField(blank=True, max_length=100, null=True, verbose_name='Student ID')),
                ('FirstName', models.CharField(max_length=100, null=True, verbose_name='First Name')),
                ('MiddleName', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name')),
                ('LastName', models.CharField(max_length=100, null=True, verbose_name='Last Name')),
                ('Gender', models.CharField(choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('DateOfBirth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('ReasonForAllowing', models.CharField(blank=True, default='Fulfilled all requirements.', max_length=100, verbose_name='Reason for Allowing')),
                ('photo', models.ImageField(default='default.png', height_field='height_field', max_length=255, upload_to='upload/%Y/%M/%D/', verbose_name="Student's Passport", width_field='width_field')),
                ('YearGroup', models.CharField(max_length=10, null=True, verbose_name='Year Group')),
                ('ClassName', models.CharField(choices=[('07B', '07B'), ('07S', '07S'), ('07I', '07I'), ('07P', '07P'), ('07R', '07R'), ('08B', '08B'), ('08S', '08S'), ('08I', '08I'), ('08P', '08P'), ('08R', '08R'), ('09B', '09B'), ('09S', '09S'), ('09I', '09I'), ('09P', '09P'), ('10B', '10B'), ('10S', '10S'), ('10I', '10I'), ('10P', '10P'), ('11B', '11B'), ('11S', '11S'), ('11I', '11I'), ('11P', '11P'), ('12B', '12B'), ('12S', '12S'), ('12I', '12I'), ('12P', '12P'), ('IFY', 'IFY')], max_length=5, null=True, verbose_name='Class Name')),
                ('Term', models.CharField(blank=True, choices=[('Select', 'Select'), ('Autumn', 'Autumn'), ('Spring', 'Spring'), ('Summer', 'Summer')], max_length=10, null=True, verbose_name='Term')),
                ('AcademicSession', models.CharField(blank=True, max_length=15, null=True, verbose_name='Academic Session')),
                ('DateOfAdmission', models.DateField(blank=True, null=True, verbose_name='Date of Admission')),
                ('Clear', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, verbose_name='Allow to check-in?')),
                ('CheckedIn', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, verbose_name='Checked-In')),
                ('CheckedOut', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, verbose_name='Checked-Out')),
                ('Parent1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Parent Name')),
                ('Parent2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Other Name')),
                ('ParentEmail', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Parent Email')),
                ('Parent1Phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Parent Phone')),
                ('Parent2Phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Other Phone')),
                ('Parent1Address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Parent Address')),
                ('Parent2Address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Other Address')),
                ('ParentPhoto', models.ImageField(default='default.png', height_field='height_field', max_length=255, upload_to='upload/%Y/%M/%D/', verbose_name="Parent's Passport", width_field='width_field')),
                ('OtherPhoto', models.ImageField(default='default.png', height_field='height_field', max_length=255, upload_to='upload/%Y/%M/%D/', verbose_name="Other's Passport", width_field='width_field')),
                ('Parent1Temp', models.CharField(blank=True, max_length=50, null=True, verbose_name='Parent Name')),
                ('Parent2Temp', models.CharField(blank=True, max_length=50, null=True, verbose_name='Other Name')),
                ('ParentEmailTemp', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Parent Email')),
                ('Parent1PhoneTemp', models.CharField(blank=True, max_length=15, null=True, verbose_name='Parent Phone')),
                ('Parent2PhoneTemp', models.CharField(blank=True, max_length=15, null=True, verbose_name='Other Phone')),
                ('Parent1AddressTemp', models.CharField(blank=True, max_length=255, null=True, verbose_name='Parent Address')),
                ('Parent2AddressTemp', models.CharField(blank=True, max_length=255, null=True, verbose_name='Other Address')),
                ('ParentPhotoTemp', models.ImageField(default='default.png', height_field='height_field', max_length=255, upload_to='upload/%Y/%M/%D/', verbose_name="Parent's Passport", width_field='width_field')),
                ('OtherPhotoTemp', models.ImageField(default='default.png', height_field='height_field', max_length=255, upload_to='upload/%Y/%M/%D/', verbose_name="Other's Passport", width_field='width_field')),
                ('Alternative', models.BooleanField(default=False, max_length=5, verbose_name='Please allow my child to be checked-in by the person whose details are provided below.')),
                ('Inbox_timestamp', models.DateTimeField(auto_now_add=True)),
                ('Approved', models.BooleanField(default=False, max_length=5, verbose_name='Approved')),
                ('CheckInTime', models.DateTimeField(blank=True, null=True)),
                ('CheckedInBy', models.CharField(max_length=50, verbose_name='Checked-In by')),
                ('CheckOutTime', models.DateTimeField(blank=True, null=True)),
                ('CheckedOutBy', models.CharField(max_length=50, verbose_name='Checked-Out by')),
                ('CheckOutSeason', models.CharField(max_length=50, verbose_name='Check-Out Season')),
            ],
            options={
                'verbose_name': 'Students',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='CurrentSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Season', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='StudentManager.Seasons')),
            ],
            options={
                'verbose_name': 'Current Season',
            },
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTimeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Check-Out Time')),
                ('ByStaff', models.CharField(blank=True, max_length=60, null=True, verbose_name='Checked-In By')),
                ('Guardian1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian 1 Accompanying')),
                ('Guardian2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian 2 Accompanying')),
                ('Guardian1Phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian 1 Phone')),
                ('Guardian2Phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian 2 Phone')),
                ('Season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManager.Seasons')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManager.Students')),
            ],
            options={
                'verbose_name': 'CheckOut',
                'verbose_name_plural': 'CheckOuts',
            },
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Passed', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, verbose_name='Allowed to Pass the Gate?')),
                ('CheckedIn', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, verbose_name='Checked into PC?')),
                ('ReasonPass', models.CharField(blank=True, max_length=200, null=True, verbose_name='Reason for Pass')),
                ('ReasonCheckInPC', models.CharField(blank=True, max_length=200, null=True, verbose_name='Reason for Check-In')),
                ('PC', models.CharField(choices=[('Pastoral Center 1', 'Pastoral Center 1'), ('Pastoral Center 2', 'Pastoral Center 2'), ('Pastoral Center 3', 'Pastoral Center 3'), ('Pastoral Center 4', 'Pastoral Center 4'), ('Pastoral Center 5', 'Pastoral Center 5'), ('Pastoral Center 6', 'Pastoral Center 6')], default='Pastoral Center 1', max_length=20, verbose_name='Pastoral Center')),
                ('Room', models.CharField(blank=True, max_length=3, null=True, verbose_name='Room Number')),
                ('Bed', models.CharField(blank=True, max_length=3, null=True, verbose_name='Bed Number')),
                ('PassCode', models.IntegerField(blank=True, null=True, verbose_name='Pass Code')),
                ('MetRequirements', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, verbose_name='Met Requirements?')),
                ('DateTimeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Check-In Time')),
                ('ByStaff', models.CharField(blank=True, max_length=60, null=True, verbose_name='Checked-In By')),
                ('Guardian1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian 1 Accompanying')),
                ('Guardian2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian 2 Accompanying')),
                ('Guardian1Phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian 1 Phone')),
                ('Guardian2Phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian 2 Phone')),
                ('Season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManager.Seasons')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManager.Students')),
            ],
            options={
                'verbose_name': 'Pass',
                'verbose_name_plural': 'CheckIns',
            },
        ),
        migrations.CreateModel(
            name='Allowed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clear', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, verbose_name='Allow to check-in?')),
                ('DateTimeStamp', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('Season', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='StudentManager.Seasons')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManager.Students')),
            ],
            options={
                'verbose_name': 'Allowed Students',
            },
        ),
    ]