# Generated by Django 5.0.1 on 2024-02-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0010_alter_requirement_virtual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
