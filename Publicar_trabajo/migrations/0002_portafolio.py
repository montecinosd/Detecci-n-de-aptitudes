# Generated by Django 2.0.4 on 2019-07-08 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Publicar_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdf')),
                ('aptitude_validadas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicar_trabajo.Aptitude_validadas')),
            ],
        ),
    ]
