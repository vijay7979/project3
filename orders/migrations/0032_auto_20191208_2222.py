# Generated by Django 2.1.5 on 2019-12-08 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20191207_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additions',
        ),
        migrations.AddField(
            model_name='order',
            name='additions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Addition'),
        ),
    ]
