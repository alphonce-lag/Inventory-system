# Generated by Django 4.0.6 on 2022-08-31 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available_product_table',
            name='product_price',
            field=models.IntegerField(),
        ),
    ]
