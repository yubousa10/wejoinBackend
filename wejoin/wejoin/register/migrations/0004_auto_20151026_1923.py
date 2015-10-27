# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20151025_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='userbase',
            field=models.OneToOneField(to='register.UserBase'),
        ),
    ]
