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
        return format_html('<img src={} width={} height={} style="max-height:150px; width:auto;"/>',
                           mark_safe(obj.image.url), obj.image.width, obj.image.height)

    fields = ('place', 'image', 'get_preview')


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ('title',)


admin.site.register(Image)
admin.site.register(Place, PlaceAdmin)
