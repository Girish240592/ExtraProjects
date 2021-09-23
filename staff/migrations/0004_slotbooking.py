# Generated by Django 3.2.6 on 2021-09-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20210921_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='slotbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centerid', models.IntegerField()),
                ('managed_by', models.CharField(max_length=20)),
                ('appointmentdate', models.DateField()),
                ('bookingdate', models.DateField()),
                ('opening_time', models.TimeField()),
                ('slot_time', models.TimeField()),
                ('booking_status', models.BooleanField()),
            ],
        ),
    ]