# Generated by Django 4.2.5 on 2023-12-05 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxout_app', '0004_alter_laxout_user_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laxout_user',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 5, 11, 0, 15, 822191, tzinfo=datetime.timezone.utc)),
        ),
    ]
