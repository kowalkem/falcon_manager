# Generated by Django 3.0.6 on 2020-05-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeding', '0007_auto_20200518_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='falcon',
            name='CITES_img',
            field=models.FileField(blank=True, null=True, upload_to='falcon_docs/'),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='RDOS_permission_img',
            field=models.FileField(blank=True, null=True, upload_to='falcon_docs/'),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='photos_old',
            field=models.ImageField(blank=True, null=True, upload_to='falcon_imgs/'),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='photos_young',
            field=models.ImageField(blank=True, null=True, upload_to='falcon_imgs/'),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='registration_img',
            field=models.FileField(blank=True, null=True, upload_to='falcon_docs/'),
        ),
    ]
