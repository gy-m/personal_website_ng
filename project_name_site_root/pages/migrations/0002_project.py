# Generated by Django 3.1 on 2020-08-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('permalink', models.CharField(max_length=32, unique=True)),
                ('description', models.TextField(blank=True)),
                ('functionality', models.CharField(max_length=1023)),
                ('server_tx', models.CharField(max_length=1024)),
                ('server_rx', models.CharField(max_length=1024)),
                ('lcd_msg', models.CharField(max_length=64)),
                ('sonar_reading', models.FloatField(max_length=64)),
                ('gps_reading', models.FloatField(max_length=64)),
                ('ir_reading', models.FloatField(max_length=64)),
                ('gyro_reading', models.FloatField(max_length=64)),
            ],
        ),
    ]
