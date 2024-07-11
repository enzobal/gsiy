from django.contrib import admin
from .models import Video
# Register your models here.


# box/admin.py fotos subidas por el admin

from django.utils.safestring import mark_safe
from .models import Foto

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida','titulo', 'imagen_tag')  # es lo que se ve en el sitio ADMIN


    def imagen_tag(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="50" height="50" />')
        return "No Image"
    imagen_tag.short_description = 'Imagen'


# videos subidos por el admin
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida', 'video_tag')

    def video_tag(self, obj):
        if obj.video:
            return mark_safe(f'<video width="200" controls><source src="{obj.video.url}" type="video/mp4"></video>')
        return "No Video"
    video_tag.short_description = 'Video'

# rutina especial
from django.contrib import admin
from .models import SpecialRoutine

@admin.register(SpecialRoutine)
class SpecialRoutineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None:
            return request.user.groups.filter(id__in=obj.visible_to_groups.values_list('id', flat=True)).exists()
        return True


# fin rutina especail