# Generated by Django 3.0.6 on 2020-05-24 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_login_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='confirm_password',
        ),
    ]
