# Generated by Django 5.1.2 on 2024-10-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='used_coupon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
