# Generated by Django 3.1.3 on 2020-11-08 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20201108_0429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='images',
            new_name='path',
        ),
    ]
