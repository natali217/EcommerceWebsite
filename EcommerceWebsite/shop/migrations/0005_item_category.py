# Generated by Django 2.2.8 on 2019-12-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20191216_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], default=2, max_length=8),
            preserve_default=False,
        ),
    ]
