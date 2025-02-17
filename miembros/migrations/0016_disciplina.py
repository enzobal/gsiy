# Generated by Django 5.0.6 on 2024-07-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0015_rename_date_posted_blogpost_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('entrenador', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='disciplinas/')),
            ],
        ),
    ]
