# Generated by Django 5.0.4 on 2024-05-07 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_itemdata_email_of_seller_itemdata_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]