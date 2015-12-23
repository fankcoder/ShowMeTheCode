# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=10000)),
                ('level', models.IntegerField(default=0, choices=[(0, b'green'), (1, b'blue'), (2, b'yellow'), (3, b'red')])),
            ],
        ),
    ]
