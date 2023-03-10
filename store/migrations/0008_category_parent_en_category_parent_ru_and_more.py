# Generated by Django 4.1.4 on 2023-02-15 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_category_en_product_category_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='store.category', verbose_name='Kategoriya'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='store.category', verbose_name='Kategoriya'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent_uz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='store.category', verbose_name='Kategoriya'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_ru',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_uz',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Kategoriyalar'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Kategoriyalar'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Kategoriyalar'),
        ),
    ]
