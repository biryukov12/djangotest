# Generated by Django 3.1.4 on 2020-12-27 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200304_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 27, 21, 53, 3, 153991)),
        ),
    ]
