# Generated by Django 5.1.1 on 2024-09-30 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodFinder', '0002_remove_restaurant_distance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Apple',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
