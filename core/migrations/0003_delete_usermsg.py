# Generated by Django 5.1 on 2024-08-20 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserMsg',
        ),
    ]