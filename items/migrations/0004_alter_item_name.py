# Generated by Django 3.2 on 2021-04-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('items', '0003_remove_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Наименование камня'),
        ),
    ]
