# Generated by Django 3.2.9 on 2021-11-29 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20211129_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='verified',
        ),
    ]
