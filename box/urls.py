from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from .views import *

# from django.contrib.auth import views

urlpatterns = [
    path('videos_insta/', videos_insta, name="videos_insta"),
    path('videos_youtube', videos_youtube, name="videos_youtube"),
    path('fotos_entrenando/', fotos_entrenando, name='fotos_entrenando'),
    path('videos_entrenando/', videos_entrenando, name='videos_entrenando'),
    #ubicacion del box
    path('ubicacion/', ubicacion, name='ubicacion'),
    # rutina para usuarios especiales
    path('ver_rutina_especial/', ver_rutina_especial, name='ver_rutina_especial'),
    # template para autorizar los grupos, hacer renderizar con link para usuario
    path('assign_group/', assign_group, name='assign_group'),
    # vista para asignar usuarios al grupo personalizado
    path('success/', success_page, name='success_page'),
    # vista del cumple de usuarios
    path('birthdays/', birthdays_view, name='birthdays_view'),
    # creacion rutina especial
    path('crear-rutina-especial/', crear_rutina_especial, name='crear_rutina_especial'),
    # fincreacion rutina esp

]

