# Generated by Django 2.2.6 on 2020-08-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManager', '0005_auto_20200818_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='DenEntryCheckIn',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, verbose_name='Deny Entry'),
        ),
    ]
