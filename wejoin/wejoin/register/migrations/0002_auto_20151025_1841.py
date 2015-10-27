# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(default=b'', max_length=30, blank=True)),
                ('email', models.EmailField(default=b'', max_length=254, blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='register',
            options={},
        ),
        migrations.RemoveField(
            model_name='register',
            name='created',
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.ForeignKey(to='register.UserBase'),
        ),
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='profile',
            field=models.TextField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
