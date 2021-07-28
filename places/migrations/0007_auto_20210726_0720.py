# Generated by Django 3.2.5 on 2021-07-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='title_on_map',
            field=models.TextField(default=11, verbose_name='Название на карте'),
            preserve_default=False,
        ),
    ]
