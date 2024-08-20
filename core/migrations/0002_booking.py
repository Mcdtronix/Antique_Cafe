# Generated by Django 5.1 on 2024-08-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField()),
                ('additional_info', models.TextField(blank=True, null=True)),
            ],
        ),
    ]