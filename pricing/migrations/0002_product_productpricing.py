# Generated by Django 4.1.5 on 2023-01-04 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pricing.pricing')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pricing.product')),
            ],
        ),
    ]
