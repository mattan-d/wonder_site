# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(max_digits=5, decimal_places=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pay_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
