# Generated by Django 5.1.4 on 2024-12-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanagementapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
