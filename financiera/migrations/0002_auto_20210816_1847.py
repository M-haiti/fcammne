# Generated by Django 3.2.6 on 2021-08-17 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0018_auto_20210816_1541'),
        ('financiera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribucioningresoic',
            name='ic',
            field=models.CharField(choices=[('SCA', 'Socias en Centroamérica'), ('FCA', 'Socias fuera de Centroamérica'), ('RFM', 'Redes y fondos de mujeres'), ('RRC', 'Respuesta Rápida en Centroamérica'), ('RRF', 'Respuesta Rápida fuera de Centroamérica'), ('OTR', 'Otros')], max_length=3, null=True, verbose_name='Iniciativa conjunta'),
        ),
        migrations.CreateModel(
            name='Desembolso',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financiera.base')),
                ('fecha_proyectada', models.DateField(null=True, verbose_name='Fecha proyectada de desembolso')),
                ('fecha_desembolso', models.DateField(null=True, verbose_name='Fecha de desembolso')),
                ('tipo_org', models.CharField(choices=[('COP', 'Coparte'), ('APE', 'Apoyo Estratégico'), ('ICJ', 'Iniciativa conjunta')], max_length=3, null=True)),
                ('numero_desembolso', models.PositiveIntegerField(null=True)),
                ('total_desembolsos', models.PositiveIntegerField(null=True)),
                ('estatus', models.CharField(choices=[('COP', 'Coparte'), ('APE', 'Apoyo Estratégico'), ('ICJ', 'Iniciativa conjunta')], max_length=3, null=True)),
                ('monto_total_USD', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Monto total USD')),
                ('monto_total_EUR', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Monto total USD')),
                ('tipo_de_cambio_EUR_USD', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Tipo de cambio (EUR -> USD)')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción')),
                ('numero_comprobante', models.CharField(max_length=255, null=True)),
                ('apoyo_estrategico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.apoyoestrategico')),
                ('ingreso_vinculado', models.ManyToManyField(to='financiera.Ingreso')),
                ('iniciativa_conjunta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.iniciativaconjunta')),
                ('propuesta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.coparte')),
            ],
            bases=('financiera.base',),
        ),
    ]
