# Generated by Django 4.2.3 on 2023-08-07 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 7, 18, 49, 37, 336902, tzinfo=datetime.timezone.utc)),
        ),
    ]
