# Generated by Django 3.2.3 on 2021-05-29 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listings_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 30, 2, 37, 19, 737181)),
        ),
    ]
