# Generated by Django 3.2.6 on 2021-08-17 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0018_auto_20210816_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropuestaIC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_prop', models.CharField(max_length=7, null=True, verbose_name='Código de la propuesta IC')),
                ('ano', models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], max_length=4, null=True, verbose_name='Año')),
                ('ic_vinculada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.iniciativaconjunta')),
            ],
        ),
        migrations.CreateModel(
            name='InformeIC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_prop', models.CharField(max_length=7, null=True, verbose_name='Informe de IC')),
                ('ano', models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], max_length=4, null=True, verbose_name='Año')),
                ('ic_vinculada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.iniciativaconjunta')),
            ],
        ),
    ]
