# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20151025_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='email',
            new_name='userbase',
        ),
    ]
