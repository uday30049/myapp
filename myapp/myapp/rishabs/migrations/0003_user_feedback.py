# Generated by Django 4.1.3 on 2022-11-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rishabs', '0002_ordermodel_is_delivered_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='feedback',
            field=models.CharField(default='', max_length=100),
        ),
    ]
