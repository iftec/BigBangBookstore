# Generated by Django 5.0.6 on 2024-07-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='Author', max_length=100),
            preserve_default=False,
        ),
    ]
