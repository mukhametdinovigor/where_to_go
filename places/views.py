import os
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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


def index(request):
    places = Place.objects.all()
    places_geojson = {'type': 'FeatureCollection',
                      'features': []}
    for place in places:
        places_geojson['features'].append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude]
                },
                'properties': {
                    'title': place.title,
                    'detailsUrl': reverse(place_detail_view, args=(place.id,))
                }
            }
        )

    context = {
        'places': places_geojson
    }
    return render(request, 'index.html', context)


def place_detail_view(request, place_id):
    requested_place = get_object_or_404(Place, id=place_id)
    place = get_place(requested_place)
    return JsonResponse(place, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})
