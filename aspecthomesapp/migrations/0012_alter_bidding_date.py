# Generated by Django 5.0.1 on 2024-02-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0011_alter_bidding_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.TimeField(auto_now=True),
        ),
    ]
