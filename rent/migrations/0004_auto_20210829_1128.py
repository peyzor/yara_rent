# Generated by Django 3.2.6 on 2021-08-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_carrent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrent',
            name='duration',
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name='carrent',
            name='rent_time',
            field=models.DateTimeField(blank=True),
        ),
    ]