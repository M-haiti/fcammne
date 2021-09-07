# Generated by Django 3.2.6 on 2021-08-16 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import programa.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programa', '0015_auto_20210816_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformeFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_prop', models.CharField(max_length=7, null=True, verbose_name='Código de la propuesta')),
                ('estatus_prop', models.CharField(choices=[('ENR', 'En revisión'), ('APR', 'Aprobado'), ('VCM', 'Ver Comentarios')], default='ACT', max_length=3, verbose_name='Estatus')),
                ('nombre_prop', models.CharField(max_length=255, null=True, verbose_name='Nombre de la propuesta')),
                ('fecha_entrega', models.DateField(null=True, verbose_name='Fecha de entrega de la propuesta')),
                ('ano', models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], max_length=4, null=True, verbose_name='Año')),
                ('fecha_periodo_init', models.DateField(null=True, verbose_name='Fecha de inicio')),
                ('fecha_periodo_finit', models.DateField(null=True, verbose_name='Fecha de finalización')),
                ('reporte_financiero', models.FileField(null=True, upload_to='%Y/reportesfinancieros', validators=[programa.models.validate_file_extension], verbose_name='Reporte Financiero (PDF)')),
                ('informe_finan_aprobado_supervisora', models.BooleanField(null=True, verbose_name='Informe financiero aprobado por oficial de programa')),
                ('informe_finan_aprobado_gestion', models.BooleanField(null=True, verbose_name='Informe financiero aprobado por oficial de gestión financiera')),
                ('estado_bancario', models.FileField(null=True, upload_to='%Y/estadosbancarios', validators=[programa.models.validate_file_extension], verbose_name='Estado bancario (PDF)')),
                ('fotografias', models.FileField(null=True, upload_to='%Y/fotografias', validators=[programa.models.validate_file_extension], verbose_name='Fotografías')),
                ('plazo', models.CharField(choices=[('12M', '12 Meses'), ('24M', '24 Meses'), ('36M', '36 Meses')], max_length=3, null=True, verbose_name='Plazo del informe final')),
                ('presupuesto_aprobado_super_USD', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Presupuesto aprobado por Supervisora FCAM (USD)')),
                ('presupuesto_aprobado_super_EUR', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Presupuesto aprobado por Supervisora FCAM (EUR)')),
                ('tipo_de_cambio_EUR_USD', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Tipo de cambio (EUR -> USD)')),
                ('monto_total_ejecutado', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Monto total ejecutado')),
                ('codigo_org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.coparte')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='informeintermedio',
            name='estado_bancario',
            field=models.FileField(null=True, upload_to='%Y/estadosbancarios', validators=[programa.models.validate_file_extension], verbose_name='Estado bancario (PDF)'),
        ),
        migrations.AddField(
            model_name='informeintermedio',
            name='fecha_periodo_finit',
            field=models.DateField(null=True, verbose_name='Fecha de finalización'),
        ),
        migrations.AddField(
            model_name='informeintermedio',
            name='fecha_periodo_init',
            field=models.DateField(null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AddField(
            model_name='informeintermedio',
            name='fotografias',
            field=models.FileField(null=True, upload_to='%Y/fotografias', validators=[programa.models.validate_file_extension], verbose_name='Fotografías'),
        ),
        migrations.AddField(
            model_name='informeintermedio',
            name='informe_finan_aprobado_gestion',
            field=models.BooleanField(null=True, verbose_name='Informe financiero aprobado por oficial de gestión financiera'),
        ),
        migrations.AddField(
            model_name='informeintermedio',
            name='informe_finan_aprobado_supervisora',
            field=models.BooleanField(null=True, verbose_name='Informe financiero aprobado por oficial de programa'),
        ),
        migrations.AddField(
            model_name='informeintermedio',
            name='propuesta_vinculada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.propuesta'),
        ),
        migrations.AddField(
            model_name='informeintermedio',
            name='reporte_financiero',
            field=models.FileField(null=True, upload_to='%Y/reportesfinancieros', validators=[programa.models.validate_file_extension], verbose_name='Reporte Financiero (PDF)'),
        ),
        migrations.AlterField(
            model_name='informeintermedio',
            name='plazo',
            field=models.CharField(choices=[('6M', '6 Meses'), ('12M', '12 Meses'), ('18M', '18 Meses'), ('30M', '30 Meses')], max_length=3, null=True, verbose_name='Plazo del informe intermedio'),
        ),
        migrations.DeleteModel(
            name='BaseInf',
        ),
        migrations.AddField(
            model_name='informefinal',
            name='informe_intermedios_anterior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.informeintermedio'),
        ),
        migrations.AddField(
            model_name='informefinal',
            name='propuesta_vinculada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.propuesta'),
        ),
        migrations.AddField(
            model_name='informefinal',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='informefinal_reponsable_propu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='informefinal',
            name='supervisora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='informefinal_supervisora_propu', to=settings.AUTH_USER_MODEL),
        ),
    ]
