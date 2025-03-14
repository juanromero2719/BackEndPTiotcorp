# Generated by Django 5.1.7 on 2025-03-07 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_limite', models.DateField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completada', 'Completada')], default='Pendiente', max_length=20)),
                ('prioridad', models.IntegerField(choices=[(1, 'Baja'), (2, 'Media'), (3, 'Alta'), (4, 'Muy Alta'), (5, 'Crítica')], default=3)),
                ('creada_en', models.DateTimeField(auto_now_add=True)),
                ('actualizada_en', models.DateTimeField(auto_now=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='personas.persona')),
            ],
        ),
    ]
