# Generated by Django 4.1 on 2023-02-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0003_furniture_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='slug',
            field=models.SlugField(default='11', unique=True),
            preserve_default=False,
        ),
    ]