# Generated by Django 3.1 on 2020-08-29 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20200829_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='function',
            name='project_functionality',
        ),
    ]
