# Generated by Django 3.1.3 on 2020-11-13 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20201108_0510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('created',), 'verbose_name': 'товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='webapp.category', verbose_name='категория'),
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('1', '1 - спальные'), ('1.5', '1.5 - спальные'), ('2', '2 - спальные')], max_length=50)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product', verbose_name='размер')),
            ],
            options={
                'verbose_name': 'размер',
                'verbose_name_plural': 'Размеры',
                'ordering': ('product_id',),
            },
        ),
    ]