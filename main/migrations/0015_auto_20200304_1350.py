# Generated by Django 3.0.3 on 2020-03-04 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200304_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 4, 13, 50, 41, 602506)),
        ),
    ]