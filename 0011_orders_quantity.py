# Generated by Django 5.0.4 on 2024-05-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_discount_orders_cart_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]