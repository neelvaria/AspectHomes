# Generated by Django 5.0.1 on 2024-02-29 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0014_remove_project_v_id_booking_designerdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='designerdate',
        ),
    ]