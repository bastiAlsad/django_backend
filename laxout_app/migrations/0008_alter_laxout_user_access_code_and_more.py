# Generated by Django 4.2.7 on 2023-12-05 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxout_app', '0007_alter_laxout_user_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laxout_user',
            name='access_code',
            field=models.CharField(default='LX-1303', max_length=10),
        ),
        migrations.AlterField(
            model_name='laxout_user',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 5, 18, 21, 18, 594945, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='laxout_user',
            name='user_uid',
            field=models.CharField(default='UP?B;dXP/1_WJ7gA4~wu95K6;hGN:;$3F\'"A*[]b55\'[ONOs?A9h%c>]D,>OCUeN@R\'&Xo%3Z>A*$7`5IwD$2JST~]hS\'|%UOBb2', max_length=80),
        ),
    ]
