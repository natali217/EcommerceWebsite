# Generated by Django 2.2.8 on 2019-12-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_item_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AlterField(
            model_name='order',
            name='ship_to',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
