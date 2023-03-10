# Generated by Django 4.1.4 on 2023-02-14 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_name_customers_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='Kategoriya'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='Kategoriya'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='Kategoriya'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, default="Tez orada bu yerda mahsulot bo'ladi", null=True, verbose_name="Batafsil ma'lumot"),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, default="Tez orada bu yerda mahsulot bo'ladi", null=True, verbose_name="Batafsil ma'lumot"),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(blank=True, default="Tez orada bu yerda mahsulot bo'ladi", null=True, verbose_name="Batafsil ma'lumot"),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Mahsulot nomi'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Mahsulot nomi'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_uz',
            field=models.CharField(max_length=300, null=True, verbose_name='Mahsulot nomi'),
        ),
    ]
