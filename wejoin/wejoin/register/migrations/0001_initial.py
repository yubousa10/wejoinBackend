# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fname', models.CharField(default=b'', max_length=30, blank=True)),
                ('lname', models.CharField(default=b'', max_length=30, blank=True)),
                ('gender', models.CharField(default=b'', max_length=10, blank=True)),
                ('email', models.CharField(default=b'', max_length=50, blank=True)),
                ('profile', models.CharField(default=b'', max_length=255, blank=True)),
                ('register_date', models.CharField(default=b'', max_length=50, blank=True)),
                ('tel', models.CharField(default=b'', max_length=16, blank=True)),
                ('zipcode', models.CharField(default=b'', max_length=10, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
