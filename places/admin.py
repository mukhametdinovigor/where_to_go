from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    extra = 0


    def get_preview(self, obj):
        return format_html('<img src={} style="max-height:150px; max-width:300px;"/>',
                           mark_safe(obj.image.url))

    fields = ('place', 'image', 'get_preview')


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ('title',)


admin.site.register(Image, ImageAdmin)
admin.site.register(Place, PlaceAdmin)
