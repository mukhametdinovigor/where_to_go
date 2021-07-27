from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        return format_html('<img src={url} width={width} height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width / 6,
            height=obj.image.height / 6,
        )
        )
    fields = ('title', 'image', 'get_preview', 'order')


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
admin.site.register(Place, PlaceAdmin)
