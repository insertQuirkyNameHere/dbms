# Generated by Django 3.2.8 on 2021-12-01 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_rename_is_superuser_customuser_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_admin',
            new_name='admin',
        ),
    ]
