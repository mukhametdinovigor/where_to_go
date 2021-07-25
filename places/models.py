from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Описание')
    description_long = models.TextField('Текст')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField('Фото')

    def __str__(self):
        return f'{self.id} {str(self.title)}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
