# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-16 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import precise_bbcode.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titre')),
                ('_corp_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('corp', precise_bbcode.fields.BBCodeTextField(no_rendered_field=True, verbose_name='texte')),
            ],
        ),
    ]
