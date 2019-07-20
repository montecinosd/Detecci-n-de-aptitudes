# Generated by Django 2.0.4 on 2019-07-20 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('declarar_SVA', '0003_portafolio_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestas',
            name='Usuario',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='Respuestas',
        ),
        migrations.AddField(
            model_name='portafolio',
            name='Usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='declarar_SVA.Persona'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='aptitude_validadas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='declarar_SVA.Aptitude_validadas'),
        ),
        migrations.DeleteModel(
            name='Respuestas',
        ),
    ]
