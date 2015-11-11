# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=100)),
                ('Publisher', models.CharField(max_length=100)),
                ('PublishDate', models.DateField()),
                ('Price', models.FloatField()),
                ('AuthorID', models.ForeignKey(to='libman.Author')),
            ],
        ),
    ]
