# Generated by Django 3.2.6 on 2021-08-06 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0002_auto_20210806_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coparte',
            old_name='contacto',
            new_name='contactos',
        ),
    ]
