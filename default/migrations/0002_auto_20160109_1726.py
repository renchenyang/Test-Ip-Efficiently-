# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historydata',
            name='ip',
            field=models.CharField(default=b'', max_length=16),
        ),
        migrations.AddField(
            model_name='historydata',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historydata',
            name='time',
            field=models.IntegerField(default=1452331579.318),
        ),
        migrations.AddField(
            model_name='todolist',
            name='ip',
            field=models.CharField(default=b'', max_length=16),
        ),
        migrations.AddField(
            model_name='todolist',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
