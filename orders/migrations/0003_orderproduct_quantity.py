# Generated by Django 3.1.3 on 2021-02-20 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210220_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
