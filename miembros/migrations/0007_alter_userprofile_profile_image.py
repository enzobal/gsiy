# Generated by Django 5.0.6 on 2024-05-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0006_alter_formulariocontacto_profesor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
