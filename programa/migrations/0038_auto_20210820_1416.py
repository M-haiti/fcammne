# Generated by Django 3.2.6 on 2021-08-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0037_auto_20210820_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informefinal',
            name='codigo_prop',
            field=models.CharField(max_length=25, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='informeintermedio',
            name='codigo_prop',
            field=models.CharField(max_length=25, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='propuesta',
            name='codigo_prop',
            field=models.CharField(max_length=25, null=True, verbose_name='Código'),
        ),
    ]
