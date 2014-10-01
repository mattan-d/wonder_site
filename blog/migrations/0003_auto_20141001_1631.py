# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_wanted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wanted',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='wanted',
            old_name='Company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='wanted',
            old_name='Position',
            new_name='position',
        ),
    ]
