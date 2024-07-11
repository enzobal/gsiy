
# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html

from .models import Actividad, Horario, UsuarioActividad, Marca, Producto, FormularioContacto, UserProfile

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'precio', 'imagen', 'cantidad_disponible', 'fecha_creacion', 'fecha_actualizacion')
    list_editable = ('nombre', 'precio', 'cantidad_disponible')
    search_fields = ('nombre', 'fecha_creacion')
    list_display_links = ('id',)

class FormularioContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'mensaje', 'correo', 'profesor', 'tipo_consulta')
    list_editable = ('nombre', 'mensaje', 'correo', 'profesor', 'tipo_consulta')
    search_fields = ('nombre',)
    list_display_links = ('id',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image_tag',  'bio', 'localidad', 'birth_date')

    def profile_image_tag(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_image.url)
        return '-'
    profile_image_tag.short_description = 'Profile Image'



class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(FormularioContacto, FormularioContactoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

class HorarioInline(admin.TabularInline):
    model = Horario
    extra = 1

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    inlines = [HorarioInline]

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'actividad', 'dia_semana', 'hora_inicio', 'hora_fin')
    list_filter = ('actividad', 'dia_semana')

@admin.register(UsuarioActividad)
class UsuarioActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'actividad', 'horario')
    list_filter = ('usuario', 'actividad')


# admin.py
from django.contrib import admin
from .models import Cuota

@admin.register(Cuota)
class CuotaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_inicio', 'fecha_vencimiento')
    search_fields = ('usuario__username',)
