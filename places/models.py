from django.db import models


class Place(models.Model):
    title_on_map = models.CharField('Название на карте', max_length=200)
    place_id = models.CharField(max_length=200)
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Описание')
    description_long = models.TextField('Текст')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('Фото', upload_to='images/')
    order = models.PositiveIntegerField('Номер', blank=True)

    def __str__(self):
        return f'{self.order} {str(self.title)}'

    class Meta:
        ordering = ['order']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
