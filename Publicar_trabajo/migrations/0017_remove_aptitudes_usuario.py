# Generated by Django 2.0.4 on 2019-07-06 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0016_aptitudes_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aptitudes',
            name='Usuario',
        ),
    ]
