# Generated by Django 2.2.6 on 2020-08-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManager', '0003_auto_20200817_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='DateTimeStampPC',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Check-In Time'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='DateTimeStamp',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Pass Time'),
        ),
    ]
