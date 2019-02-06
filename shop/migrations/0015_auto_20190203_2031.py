# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-03 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Order'),
        ),
    ]
