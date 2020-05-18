# Generated by Django 3.0.6 on 2020-05-18 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breeding', '0003_auto_20200515_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aviary',
            name='falcons',
            field=models.ManyToManyField(blank=True, to='breeding.Falcon'),
        ),
        migrations.AlterField(
            model_name='aviary',
            name='pair',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='breeding.Pair'),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='siblings',
            field=models.ManyToManyField(blank=True, related_name='_falcon_siblings_+', to='breeding.Falcon'),
        ),
        migrations.AlterField(
            model_name='pair',
            name='offspring',
            field=models.ManyToManyField(blank=True, to='breeding.Falcon'),
        ),
    ]
