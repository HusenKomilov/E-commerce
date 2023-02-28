# Generated by Django 4.1.4 on 2023-02-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customers_order_shippingaddress_orderproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Buyurtma tovari', 'verbose_name_plural': 'Buyurtma tovarlari'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'Адрес доставки', 'verbose_name_plural': 'Адреса доставки'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='created_ad',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='added_ad',
            new_name='added_at',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='created_ad',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='customers',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Elektron manzil'),
        ),
    ]