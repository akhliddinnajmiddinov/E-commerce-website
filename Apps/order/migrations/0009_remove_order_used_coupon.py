# Generated by Django 5.1.2 on 2024-10-26 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='used_coupon',
        ),
    ]