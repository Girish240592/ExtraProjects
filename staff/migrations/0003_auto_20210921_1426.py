# Generated by Django 3.2.6 on 2021-09-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_addoperator'),
    ]

    operations = [
        migrations.CreateModel(
            name='addstaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobileno', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=3)),
                ('loginid', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='addoperator',
            name='centername',
            field=models.CharField(max_length=200, verbose_name='Center Name'),
        ),
        migrations.AlterField(
            model_name='addoperator',
            name='operatorname',
            field=models.CharField(max_length=100, verbose_name='Operator Name'),
        ),
    ]