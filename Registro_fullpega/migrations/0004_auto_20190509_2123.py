# Generated by Django 2.0.4 on 2019-05-09 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro_fullpega', '0003_auto_20190507_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='privilegio',
            field=models.CharField(choices=[('Sp', 'Sin_privilegios'), ('Po', 'Privilegio_ofrecer'), ('Pp', 'Privilegio_publicar'), ('Pm', 'Privilegio_mutuo')], default='Sp', max_length=4),
        ),
    ]
