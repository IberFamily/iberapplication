# Generated by Django 3.2.7 on 2021-10-21 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20211021_0417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='na_cenkanju',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='odbijeno',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='prihvaćeno',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Na čekanju', 'Na čekanju'), ('Prihvaćeno', 'Prihvaćeno'), ('Odbijeno', 'Odbijeno')], default='Na čekanju', max_length=200),
        ),
    ]
