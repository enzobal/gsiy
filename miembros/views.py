from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Producto, UserProfile, Actividad, UsuarioActividad
from .forms import FormularioContactoForm, CustomUserCreationForm, UsuarioActividadForm
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from datetime import timedelta

def inicio(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'inicio.html', data)





def home(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'home.html', data)

def contacto(request):
    data = {'form': FormularioContactoForm()}
    if request.method == 'POST':
        formulario = FormularioContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje de contacto guardado"
        else:
            data["form"] = formulario
    return render(request, 'contacto.html', data)

def galeria(request):
        productos = Producto.objects.all()
        veremos= {'productos': productos}
        return render(request, 'galeria.html',veremos)

@login_required
def perfil(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    usuario_actividades = UsuarioActividad.objects.filter(usuario=request.user)
    return render(request, 'perfil.html', {
        'user_profile': user_profile,
        'usuario_actividades': usuario_actividades
    })

def registro(request):
    data = {'formContac': CustomUserCreationForm()}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            user = formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, "Te registraste correctamente")
                return redirect('home')
        else:
            data['formContac'] = formulario
    return render(request, 'registration/registro.html', data)

def admin_required(login_url=None):
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)

@admin_required(login_url='/login/')
def lista_usuarios(request):
    usuarios = User.objects.all().select_related('userprofile')
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def seleccionar_actividad(request):
    if request.method == 'POST':
        form = UsuarioActividadForm(request.POST)
        if form.is_valid():
            usuario_actividad = form.save(commit=False)
            usuario_actividad.usuario = request.user
            usuario_actividad.save()
            messages.success(request, "Actividad seleccionada correctamente")
            return redirect('perfil')
    else:
        form = UsuarioActividadForm()
    return render(request, 'seleccionar_actividad.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileUpdateForm, UserUpdateForm

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito')
            return redirect('perfil')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.userprofile)

    return render(request, 'update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cuota
from .forms import CuotaForm

@login_required
def cuota_view(request):
    cuotas = Cuota.objects.filter(usuario=request.user)
    return render(request, 'cuota_detail.html', {'cuotas': cuotas, 'is_superuser': request.user.is_superuser})


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Cuota
from .forms import CuotaForm
from django.db.models import Q

@user_passes_test(lambda u: u.is_superuser)
def cuota_admin_view(request):
    cuotas = Cuota.objects.all()
    query = request.GET.get('q')

    if query:
        # Filtrar por usuario o estado de pago
        cuotas = cuotas.filter(
            Q(usuario__username__icontains=query) |
            Q(pagada=True if query.lower() == 'verdadero' else False)
        )

    return render(request, 'cuota_admin.html', {'cuotas': cuotas})




@login_required
def cuota_edit_view(request, pk):
    if not request.user.is_superuser:
        return redirect('home')

    cuota = get_object_or_404(Cuota, pk=pk)
    if request.method == "POST":
        form = CuotaForm(request.POST, instance=cuota)
        if form.is_valid():
            form.save()
            return redirect('cuota_admin')  # Asegúrate de tener esta vista y URL configuradas
    else:
        form = CuotaForm(instance=cuota)

    return render(request, 'cuota_edit.html', {'form': form})

@login_required
def cuota_create_view(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == "POST":
        form = CuotaForm(request.POST)
        if form.is_valid():
            cuota = form.save(commit=False)
            if not cuota.fecha_vencimiento:
                cuota.fecha_vencimiento = cuota.fecha_inicio + timedelta(days=30)
            cuota.save()

            # Enviar correo electrónico al usuario
            user_email = cuota.usuario.email
            send_mail(
                'Cuota Creada',
                'Se ha creado una nueva cuota para ti.',
                'your_email@example.com',  # Cambia esto por tu dirección de correo
                [user_email],
                fail_silently=False,
            )
            return redirect('cuota_admin')
    else:
        form = CuotaForm()

    return render(request, 'cuota_create.html', {'form': form})


@login_required
def cuota_pagar_view(request, pk):
    if not request.user.is_superuser:
        return redirect('home')

    cuota = get_object_or_404(Cuota, pk=pk)
    cuota.pagada = True
    cuota.save()

    # Enviar correo electrónico al usuario
    user_email = cuota.usuario.email
    send_mail(
        'Cuota Pagada',
        'Tu cuota ha sido pagada exitosamente.',
        'your_email@example.com',  # Cambia esto por tu dirección de correo
        [user_email],
        fail_silently=False,
    )

    return redirect('cuota_admin')


# para agregar modificar cuota si se equivoca el admin
# views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Cuota
from django.core.mail import send_mail
from datetime import timedelta

@user_passes_test(lambda u: u.is_superuser)
def toggle_pagada(request, pk):
    cuota = get_object_or_404(Cuota, pk=pk)
    cuota.pagada = not cuota.pagada
    cuota.save()

    # Envía un correo electrónico al usuario
    subject = 'Cambio de estado de la cuota'
    message = f'Se ha cambiado el estado de la cuota con ID {cuota.pk} a {"Pagado" if cuota.pagada else "Sin pagar"}.'
    from_email = 'your_email@example.com'  # Cambia esto por tu dirección de correo
    to_email = cuota.usuario.email
    send_mail(subject, message, from_email, [to_email], fail_silently=False)

    return redirect('cuota_admin')

# fin de modificar cuota pagada o no si se equivoca admin

# para el blog del home
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'blog_post_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def blog_post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_post_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def blog_post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog_post_confirm_delete.html', {'post': post})

@login_required
def blog_post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_post_form.html', {'form': form})

@login_required
def blog_post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog_post_confirm_delete.html', {'post': post})



#fin del blog del home