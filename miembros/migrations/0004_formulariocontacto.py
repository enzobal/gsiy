# Generated by Django 5.0.6 on 2024-05-14 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.CharField(choices=[(0, 'Consulta general'), (1, 'Reclamo'), (2, 'Sugerencias'), (3, 'Felicitarnos por')], max_length=100)),
                ('profesor', models.CharField(choices=[(0, 'GAP'), (1, 'JU JITSU'), (2, 'CROSFIT'), (3, 'FUNCIONAL KIDS')], max_length=100)),
                ('mensaje', models.TextField()),
                ('aviso', models.BooleanField(default=False)),
            ],
        ),
    ]
