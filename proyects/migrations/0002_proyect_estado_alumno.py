# Generated by Django 5.1.4 on 2024-12-04 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyect',
            name='estado_alumno',
            field=models.CharField(default='Inactivo', max_length=50),
        ),
    ]
