# Generated by Django 3.0.3 on 2020-03-04 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200304_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 4, 9, 29, 20, 286988, tzinfo=utc)),
        ),
    ]