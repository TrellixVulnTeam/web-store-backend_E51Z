# Generated by Django 3.1.3 on 2021-02-20 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='user_id',
            new_name='user',
        ),
    ]
