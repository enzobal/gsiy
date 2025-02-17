# Generated by Django 5.0.6 on 2024-05-28 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0010_discipline'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(max_length=20)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miembros.actividad')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioActividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miembros.actividad')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miembros.horario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
