# Generated by Django 2.0.2 on 2021-01-25 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0015_auto_20200126_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 10, 53, 7, 228972, tzinfo=utc)),
        ),
    ]
