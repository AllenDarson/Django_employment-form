# Generated by Django 5.2.3 on 2025-06-30 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_sqlform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_detail',
            name='address',
        ),
    ]
