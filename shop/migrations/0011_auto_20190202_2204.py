# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-02 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_cart_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dateOfPurchase',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paymentDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]