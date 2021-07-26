import os
from django.shortcuts import render
from places.models import Place


# def get_images_path(place):
#     images = []
#     for img in place.images.all():
#         images.append(os.path.join('media', img.image))
#     return images
#
#
# def get_place(place):
#     return {
#         'title': place.title,
#         'imgs': get_images_path(place),
#         'description_short': place.description_short,
#         'description_long': place.description_long,
#         'coordinates': {
#             'lng': place.longitude,
#             'lat': place.latitude
#         }
#     }
def serialize_place(place):
    return {
        'title': place.title_on_map,
        'placeId': place.place_id,
        'coordinates': [place.longitude, place.latitude]
    }


def index(request):
    places = Place.objects.all()
    context = {
        'places': [
            serialize_place(place) for place in places
        ]
    }
    return render(request, 'index.html', context)
