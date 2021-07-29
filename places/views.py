import os
from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import JsonResponse


def get_images_path(place):
    images = []
    for img in place.images.all():
        images.append((os.path.join('media', img.image.url)))
    return images


def get_place(place):
    return {
        'title': place.title,
        'imgs': get_images_path(place),
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }


def serialize_place(place):
    return {
        'title': place.title,
        'coordinates': [place.longitude, place.latitude],
        'id': place.id
    }


def index(request):
    places = Place.objects.all()
    context = {
        'places': [
            serialize_place(place) for place in places
        ]
    }
    return render(request, 'index.html', context)


def place_detail_view(request, place_id):
    requested_place = get_object_or_404(Place, id=place_id)
    place = get_place(requested_place)
    return JsonResponse(place, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})
