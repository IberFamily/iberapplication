# Generated by Django 3.2.5 on 2021-11-01 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_vendor_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='image',
            new_name='images',
        ),
    ]