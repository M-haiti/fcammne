# Generated by Django 3.2.6 on 2021-08-19 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0030_auto_20210819_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informefinal',
            old_name='codigo',
            new_name='codigo_prop',
        ),
        migrations.RenameField(
            model_name='informeintermedio',
            old_name='codigo',
            new_name='codigo_prop',
        ),
        migrations.RenameField(
            model_name='propuesta',
            old_name='codigo',
            new_name='codigo_prop',
        ),
    ]
