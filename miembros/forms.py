from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FormularioContacto, UserProfile, UsuarioActividad

class FormularioContactoForm(forms.ModelForm):
    class Meta:
        model = FormularioContacto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    profile_image = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'profile_image']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile_image = self.cleaned_data.get('profile_image')
            UserProfile.objects.create(user=user, profile_image=profile_image)
        return user

class UsuarioActividadForm(forms.ModelForm):
    class Meta:
        model = UsuarioActividad
        fields = ['actividad', 'horario']


from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'localidad', 'birth_date']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# forms.py
from django import forms
from .models import Cuota

class CuotaForm(forms.ModelForm):
    class Meta:
        model = Cuota
        fields = ['usuario','fecha_inicio']


#del blog del home
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'video']

#fin del blog del home



