# Generated by Django 5.0.1 on 2024-03-02 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0018_billing_cname'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='dname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aspecthomesapp.requirement'),
        ),
    ]
