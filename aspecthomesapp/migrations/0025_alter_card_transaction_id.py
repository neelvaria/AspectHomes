# Generated by Django 5.0.1 on 2024-03-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0024_alter_card_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='transaction_id',
            field=models.BigIntegerField(default='', null=True),
        ),
    ]
