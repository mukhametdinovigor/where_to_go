from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    extra = 0


    def get_preview(self, obj):
        return format_html('<img src={url} width={width} height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width / 6,
            height=obj.image.height / 6,
        ))

    fields = ('title', 'image', 'get_preview')


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
admin.site.register(Place, PlaceAdmin)
