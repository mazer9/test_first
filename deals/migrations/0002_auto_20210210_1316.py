# Generated by Django 2.2.18 on 2021-02-10 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_squashed_0002_auto_20210210_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество товара, шт'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]