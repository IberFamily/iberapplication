# Generated by Django 3.2.5 on 2021-10-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_orderitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='panelStatus',
            field=models.BooleanField(default=False),
        ),
    ]
