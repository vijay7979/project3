# Generated by Django 2.1.5 on 2019-12-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_remove_order_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='special',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
