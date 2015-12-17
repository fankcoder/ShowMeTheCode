# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commapp', '0002_auto_20151012_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('comments', models.CharField(max_length=1200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='comdata',
        ),
    ]
