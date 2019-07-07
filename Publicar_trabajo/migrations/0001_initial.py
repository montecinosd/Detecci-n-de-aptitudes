# Generated by Django 2.0.4 on 2019-07-07 11:24

import Publicar_trabajo.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aptitude_validadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Aptitudes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to=Publicar_trabajo.models.content_file_name)),
                ('Nombre', models.CharField(blank=True, max_length=120, null=True)),
                ('Descripccion', models.TextField()),
                ('Fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aptitud_vinculada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Aptitudes')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comuna', models.CharField(blank=True, max_length=50, null=True)),
                ('Pais', models.CharField(blank=True, max_length=50, null=True)),
                ('Ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('Calle', models.CharField(blank=True, max_length=100, null=True)),
                ('Numero_de_calle', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=120, null=True)),
                ('Rut', models.CharField(blank=True, max_length=20, null=True)),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to=Publicar_trabajo.models.content_file_name)),
                ('Telefono_C', models.CharField(blank=True, max_length=50, null=True)),
                ('Correo', models.CharField(blank=True, max_length=100, null=True)),
                ('Direccion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Direccion')),
                ('Usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(blank=True, max_length=100, null=True)),
                ('a', models.CharField(blank=True, max_length=100, null=True)),
                ('b', models.CharField(blank=True, max_length=100, null=True)),
                ('c', models.CharField(blank=True, max_length=100, null=True)),
                ('d', models.CharField(blank=True, max_length=100, null=True)),
                ('Respuesta_correcta', models.CharField(blank=True, max_length=10, null=True)),
                ('Aptitud_vinculada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Aptitudes')),
                ('Cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Cuestionario')),
            ],
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Informacion', models.TextField()),
                ('Validez', models.BooleanField()),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='Respuestas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Respuestas'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='Usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aptitudes',
            name='Area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Areas'),
        ),
        migrations.AddField(
            model_name='aptitudes',
            name='Usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aptitude_validadas',
            name='Aptitud_validada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Aptitudes'),
        ),
        migrations.AddField(
            model_name='aptitude_validadas',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Persona'),
        ),
    ]
