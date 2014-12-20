# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favIngredients',
            field=jsonfield.fields.JSONField(default={b'favIngredients': [b'', b'', b'']}, blank=True),
            preserve_default=True,
        ),
    ]
