# Generated by Django 3.2.8 on 2021-12-01 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211201_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_superuser',
            new_name='is_admin',
        ),
    ]
