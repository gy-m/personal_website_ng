# Generated by Django 3.1 on 2020-08-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20200828_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensors',
            name='led_1',
            field=models.BooleanField(default=False),
        ),
    ]
