# Generated by Django 4.2.1 on 2023-05-21 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointmentCreation', '0002_rename_patientrecords_patientrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientrecord',
            old_name='Doctor',
            new_name='doctor',
        ),
    ]