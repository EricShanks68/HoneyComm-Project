# Generated by Django 4.2.4 on 2023-08-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_alter_cart_products_alter_product_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, default='place_holder_book.png', null=True, upload_to=''),
        ),
    ]