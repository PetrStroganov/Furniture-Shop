# Generated by Django 4.1 on 2022-12-19 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='furniture_type', to='furniture.furnituretype'),
        ),
    ]
