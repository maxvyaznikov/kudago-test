# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0002_auto_20160528_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='metro',
        ),
        migrations.AddField(
            model_name='place',
            name='metro',
            field=models.ManyToManyField(to='afisha.Metro'),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='afisha.Event'),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='url',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='afisha.Place'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='url',
            field=models.CharField(max_length=1024),
        ),
    ]
