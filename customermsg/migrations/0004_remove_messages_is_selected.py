# Generated by Django 3.2.5 on 2021-11-04 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customermsg', '0003_auto_20211104_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='is_selected',
        ),
    ]
