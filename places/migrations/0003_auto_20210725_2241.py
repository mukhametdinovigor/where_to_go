# Generated by Django 3.2.5 on 2021-07-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['id'], 'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/images/', verbose_name='Фото'),
        ),
        migrations.AlterIndexTogether(
            name='image',
            index_together=set(),
        ),
    ]
