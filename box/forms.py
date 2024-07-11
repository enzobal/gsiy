from django import forms
from django.contrib.auth.models import Group
from .models import SpecialRoutine

class SpecialRoutineForm(forms.ModelForm):
    class Meta:
        model = SpecialRoutine
        fields = ['name', 'description', 'visible_to_groups']
    
    visible_to_groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

from django import forms
from django.contrib.auth.models import Group, User

class AssignGroupForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    group = forms.ModelChoiceField(queryset=Group.objects.all())

