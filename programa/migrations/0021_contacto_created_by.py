# Generated by Django 3.2.6 on 2021-08-17 18:05

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programa', '0020_auto_20210817_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL), 
        ),
    ]
