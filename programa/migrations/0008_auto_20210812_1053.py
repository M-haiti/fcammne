# Generated by Django 3.2.6 on 2021-08-12 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programa', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='IniciativaConjunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(choices=[('GTM', 'Guatemala'), ('PAN', 'Panamá'), ('SLV', 'El Salvador'), ('HND', 'Honduras'), ('BLZ', 'Belize'), ('NIC', 'Nicaragua'), ('CRI', 'Costa Rica'), ('OTR', 'Otro')], max_length=3)),
                ('codigo_org', models.CharField(max_length=7, verbose_name='Código de organización')),
                ('nombre_org', models.CharField(max_length=255)),
                ('estatus_org', models.CharField(choices=[('ACT', 'Activo'), ('TER', 'Terminado')], default='ACT', max_length=3)),
                ('sello_fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('sello_fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_completado', models.DateField(null=True)),
                ('municipio', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('sitio_web', models.CharField(max_length=255)),
                ('fecha_grupo', models.DateField(null=True)),
                ('personeria', models.BooleanField(null=True)),
                ('fecha_personeria', models.DateField(null=True)),
                ('informacion_bancaria', models.TextField(null=True)),
                ('tipo_ic', models.CharField(choices=[('SCA', 'Socias en Centroamérica'), ('FCA', 'Socias fuera de Centroamérica'), ('RFM', 'Redes y fondos de mujeres'), ('RRC', 'Respuesta Rápida en Centroamérica'), ('RRF', 'Respuesta Rápida fuera de Centroamérica'), ('OTR', 'Otros')], max_length=3)),
                ('supervisora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
