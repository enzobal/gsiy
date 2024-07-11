from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
from django.contrib.auth import views

urlpatterns = [
    path('',home,name='home'),
    path('perfil/',perfil,name='perfil'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('lista-usuarios/', lista_usuarios, name='lista_usuarios'),
    path('seleccionar-actividad/', seleccionar_actividad, name='seleccionar_actividad'),
    path('update_profile/', update_profile, name='update_profile'),
    path('cuota/', cuota_view, name='cuota_view'),
    path('cuota/admin/', cuota_admin_view, name='cuota_admin'),
    path('cuota/<int:pk>/editar/', cuota_edit_view, name='cuota_edit'),
    # path('modificar_perfil/', views.update_profile, name='modificar_perfil'),
    path('cuota/<int:pk>/edit/', cuota_edit_view, name='cuota_edit'),
    path('cuota/create/', cuota_create_view, name='cuota_create'),
    path('cuota/<int:pk>/pagar/', cuota_pagar_view, name='cuota_pagar'),
    path('inicio/',inicio,name='inicio'),
    # modificar cuota pagada o no si se equivoca admin
    path('cuota/<int:pk>/toggle_pagada/', toggle_pagada, name='toggle_pagada'),
    # fin modificar cuota o no
#para el blog del home
    path('new/', blog_post_create, name='blog_post_create'),
    path('edit/<int:pk>/', blog_post_edit, name='blog_post_edit'),
    path('delete/<int:pk>/', blog_post_delete, name='blog_post_delete'),
#fin del blog del home
# para agregar fotos de las disciplinas
    # path('agregar_disciplina/', agregar_disciplina, name='agregar_disciplina'),
    # path('lista_disciplinas/', lista_disciplinas, name='lista_disciplinas'),
    # fin agregar fotso discilipnas
    
    
    

]