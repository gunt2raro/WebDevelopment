# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebDevelopment', '0002_auto_20150723_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(default=b'url', max_length=200, null=True),
            preserve_default=True,
        ),
    ]
