# Generated by Django 3.2.5 on 2021-07-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20210726_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='title_on_map',
            field=models.CharField(max_length=200, verbose_name='Название на карте'),
        ),
    ]