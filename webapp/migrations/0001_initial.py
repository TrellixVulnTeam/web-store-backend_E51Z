# Generated by Django 3.1.3 on 2021-02-20 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='категория')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='наименование')),
                ('brief_description', models.TextField(default='', verbose_name='краткое описание')),
                ('description', models.TextField(default='', verbose_name='описание')),
                ('price', models.PositiveIntegerField(verbose_name='цена')),
                ('size', models.CharField(blank=True, max_length=20, verbose_name='размер')),
                ('color', models.CharField(blank=True, max_length=16, verbose_name='цвет')),
                ('views', models.PositiveBigIntegerField(default=0, verbose_name='просмотры')),
                ('quantity_stock', models.IntegerField(default=0, verbose_name='кол-во на складе')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('barcode', models.IntegerField(blank=True, default='', unique=True, verbose_name='код товара')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='подкатегория')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sub', to='webapp.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'подкатегория',
                'verbose_name_plural': 'подкатегории',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('if_like', models.BooleanField(default=1)),
                ('review_text', models.TextField(max_length=1000)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('for_product_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webapp.product')),
                ('from_user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('from_user_id',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webapp.subcategory', verbose_name='подкатегория'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(default='', max_length=500)),
                ('image_name', models.CharField(default='', max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img', to='webapp.product')),
            ],
            options={
                'verbose_name': 'картинка',
                'verbose_name_plural': 'Картинки',
                'ordering': ('product_id',),
            },
        ),
    ]
