# Generated by Django 3.2.5 on 2021-07-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_auto_20210729_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Фото'),
        ),
    ]
