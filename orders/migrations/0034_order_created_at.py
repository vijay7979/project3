# Generated by Django 2.1.5 on 2019-12-23 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0033_auto_20191212_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
