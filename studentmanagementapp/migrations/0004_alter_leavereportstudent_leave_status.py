# Generated by Django 5.1.4 on 2025-01-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanagementapp', '0003_alter_attendance_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]
