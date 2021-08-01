from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField('Название', max_length=200, blank=True)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = tinymce_models.HTMLField('Полное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.ForeignKey(Place,
                              related_name='images',
                              on_delete=models.CASCADE,
                              verbose_name='Название фото')
    image = models.ImageField('Фото', upload_to='images/', blank=True)
    order = models.PositiveIntegerField('Номер', default=0, blank=True)

    def __str__(self):
        return f'{self.order} {str(self.title)}'

    class Meta:
        ordering = ['order']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
