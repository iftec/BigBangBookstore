# Generated by Django 5.1.1 on 2024-09-09 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_order_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='house',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ship_house',
        ),
    ]
