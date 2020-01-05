# Generated by Django 2.1.5 on 2019-11-30 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20191130_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pasta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Pasta'),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='category',
            field=models.CharField(max_length=64),
        ),
    ]
