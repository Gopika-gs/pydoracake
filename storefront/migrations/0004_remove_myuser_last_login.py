# Generated by Django 4.0.3 on 2022-04-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0003_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='last_login',
        ),
    ]
