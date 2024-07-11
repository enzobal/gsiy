from django.shortcuts import render
from .models import Foto
from .models import Video

# Create your views here.




def videos_insta(request):
    return render(request, 'videos_insta.html')

def videos_youtube(request):
    return render(request, 'videos_youtube.html')


#  fotos de entrnamiento subidos por el admin
def fotos_entrenando(request):
    fotos = Foto.objects.all()
    return render(request, 'fotos_entrenando.html', {'fotos': fotos})


# videos subidos por el admin
def videos_entrenando(request):
    videos = Video.objects.all()
    return render(request, 'videos_entrenando.html', {'videos': videos})

#mapa de ubicacion del box
def ubicacion(request):
    return render(request, 'ubicacion.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import SpecialRoutineForm
from .models import SpecialRoutine

# vista para ver los usuarios  en cada grupo de rutina especial
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SpecialRoutine
from django.http import HttpResponseForbidden

from django.shortcuts import render, redirect

@login_required
def ver_rutina_especial(request):
    grupo_autorizado = 'Autorizados'  # Nombre del grupo autorizado
    print(f"Usuario: {request.user.username}")
    print(f"Superuser: {request.user.is_superuser}")
    print(f"Grupos: {[group.name for group in request.user.groups.all()]}")

    if not request.user.is_superuser and not request.user.groups.filter(name=grupo_autorizado).exists():
        return render(request, 'no_permiso.html')

    # Ordenar las rutinas por fecha de creación descendente
    rutinas = SpecialRoutine.objects.order_by('-created_at')

    return render(request, 'ver_rutina_especial.html', {'rutinas': rutinas})



from django.shortcuts import render, redirect
from .forms import AssignGroupForm
# fin rutina especial

# vista para elegri los uaurios en los grulpos
def assign_group(request):
    if request.method == 'POST':
        form = AssignGroupForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            group = form.cleaned_data['group']
            user.groups.add(group)
            return redirect('success_page')  # Redirige a una página de éxito
    else:
        form = AssignGroupForm()
    return render(request, 'assign_group.html', {'form': form})

# vista de exito que es lo que redirecciona arriba
from django.shortcuts import render

def success_page(request):
    return render(request, 'success.html')
# fin de vista de exito



# para renderizar cumples

from datetime import date, timedelta
from django.shortcuts import render
from django.contrib.auth.models import User
from miembros.models import UserProfile

def birthdays_view(request):
    today = date.today()
    users_with_birthday_today = User.objects.filter(userprofile__birth_date__month=today.month, userprofile__birth_date__day=today.day)
    upcoming_birthdays = User.objects.filter(userprofile__birth_date__gt=today).order_by('userprofile__birth_date')[:10]

    context = {
        'users_with_birthday_today': users_with_birthday_today,
        'upcoming_birthdays': upcoming_birthdays,
    }
    return render(request, 'birthdays.html', context)

# fin cumples


# para crear una rutina especial
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SpecialRoutineForm

@user_passes_test(lambda u: u.is_superuser)
@login_required
def crear_rutina_especial(request):
    if request.method == 'POST':
        form = SpecialRoutineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_rutina_especial')
    else:
        form = SpecialRoutineForm()
    
    return render(request, 'crear_rutina_especial.html', {'form': form})

# fin de rutina espacial