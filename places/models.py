from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = tinymce_models.HTMLField('Полное описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place,
                              related_name='images',
                              on_delete=models.CASCADE,
                              verbose_name='Наименование места')
    image = models.ImageField('Фото', upload_to='images/')
    order = models.PositiveIntegerField('Номер', default=0, blank=True)

    def __str__(self):
        return f'{self.order} {str(self.place)}'

    class Meta:
        ordering = ['order']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
