# Generated by Django 2.2.8 on 2019-12-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
