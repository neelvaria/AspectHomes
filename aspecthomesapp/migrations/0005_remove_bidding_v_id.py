# Generated by Django 5.0.1 on 2024-02-17 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0004_alter_requirement_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidding',
            name='v_id',
        ),
    ]