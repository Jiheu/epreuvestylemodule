# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.AddField(
            model_name='document',
            name='longueur_analyse_energie',
            field=models.FloatField(default=0.01),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='longueur_analyse_harmonique_frequence_fondamentale',
            field=models.FloatField(default=0.01),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='longueur_fenetre_formant',
            field=models.FloatField(default=0.01),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='pas_analyse_energie',
            field=models.FloatField(default=0.01),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='pas_analyse_harmonique_frequence_fondamentale',
            field=models.FloatField(default=0.01),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='pas_analyse_segmentation',
            field=models.FloatField(default=0.01),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='seuil_segmentation',
            field=models.FloatField(default=0.01),
            preserve_default=False,
        ),
    ]