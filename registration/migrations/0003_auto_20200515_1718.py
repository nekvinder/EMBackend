# Generated by Django 3.0.6 on 2020-05-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20200515_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
