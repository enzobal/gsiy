# Generated by Django 5.0.6 on 2024-06-27 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
