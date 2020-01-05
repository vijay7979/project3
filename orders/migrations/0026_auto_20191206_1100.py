# Generated by Django 2.1.5 on 2019-12-06 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_addition_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additions',
        ),
        migrations.AddField(
            model_name='order',
            name='additions',
            field=models.ManyToManyField(blank=True, to='orders.Addition'),
        ),
    ]
