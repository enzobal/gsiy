# Generated by Django 5.0.6 on 2024-05-27 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0009_rename_location_userprofile_localidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
