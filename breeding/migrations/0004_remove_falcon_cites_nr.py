# Generated by Django 3.0.7 on 2021-05-03 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breeding', '0003_auto_20210502_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='falcon',
            name='CITES_nr',
        ),
    ]
