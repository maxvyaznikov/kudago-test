# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=256)),
                ('has_price', models.BooleanField()),
                ('type', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('age_restricted', models.CharField(blank=True, max_length=3, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afisha.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('phones', models.TextField(blank=True, null=True)),
                ('work_time', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afisha.Place')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=5)),
                ('time_till', models.CharField(blank=True, max_length=5, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afisha.Event')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afisha.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='metro',
            field=models.ManyToManyField(to='afisha.Metro'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='afisha.Tag'),
        ),
    ]
