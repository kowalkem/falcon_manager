# Generated by Django 3.0.7 on 2020-10-02 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breeding', '0020_pair_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pair',
            name='offspring',
        ),
        migrations.AlterField(
            model_name='falcon',
            name='in_pair',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='_pair', to='breeding.Pair'),
        ),
    ]