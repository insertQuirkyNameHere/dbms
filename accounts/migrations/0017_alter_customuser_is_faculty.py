# Generated by Django 3.2.8 on 2021-12-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_customuser_is_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_faculty',
            field=models.BooleanField(default=False),
        ),
    ]