# Generated by Django 4.1.5 on 2023-01-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0005_alter_pricing_products_alter_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='productprice',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
