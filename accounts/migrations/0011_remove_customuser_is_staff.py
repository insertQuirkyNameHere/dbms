# Generated by Django 3.2.8 on 2021-12-01 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_is_admin_customuser_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
    ]
