# Generated by Django 3.2.15 on 2022-09-20 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20220919_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
