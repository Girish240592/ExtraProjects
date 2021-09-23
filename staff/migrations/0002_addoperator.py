# Generated by Django 3.2.6 on 2021-09-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addoperator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centername', models.CharField(max_length=200)),
                ('operatorname', models.CharField(max_length=100)),
                ('operatormob', models.CharField(max_length=20)),
                ('loginid', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
            ],
        ),
    ]