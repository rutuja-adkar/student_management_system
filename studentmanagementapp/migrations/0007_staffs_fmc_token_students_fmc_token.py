# Generated by Django 5.1.4 on 2025-01-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanagementapp', '0006_onlineclassroom_studentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='fmc_token',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='students',
            name='fmc_token',
            field=models.TextField(default=''),
        ),
    ]
