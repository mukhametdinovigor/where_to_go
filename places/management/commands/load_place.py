import requests
import os
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from places.models import Place


class Command(BaseCommand):
    help = 'Upload place to database'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def download_image(self, image_url, folder):
        os.makedirs(folder, exist_ok=True)
        img_name = os.path.basename(image_url)
        img_path = os.path.join(os.getcwd(), folder, img_name)
        response = requests.get(image_url)
        response.raise_for_status()
        with open(img_path, 'wb') as img:
            img.write(response.content)
        return img_path

    def handle(self, *args, **kwargs):
        place_url = kwargs['url']
        response = requests.get(place_url)
        response.raise_for_status()
        place_attrs = response.json()
        Place.objects.get_or_create(
            title=response.json()['title'],
            description_short=place_attrs['description_short'],
            description_long=place_attrs['description_long'],
            longitude=place_attrs['coordinates']['lng'],
            latitude=place_attrs['coordinates']['lat']
        )
        img_order_field = 1
        folder = 'media/downloaded_images'
        for img_url in response.json()['imgs']:
            image = get_object_or_404(Place, title=response.json()['title']).images.\
                get_or_create(place=response.json()['title'], order=img_order_field)
            img_to_upload = open(self.download_image(img_url, folder), 'rb')
            image[0].image.save(os.path.basename(img_url), img_to_upload, save=True)
            img_order_field += 1
