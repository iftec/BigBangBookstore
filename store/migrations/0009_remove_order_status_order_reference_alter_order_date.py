# Generated by Django 5.0.6 on 2024-07-17 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_orderitems_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='reference',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_created=True),
        ),
    ]
