# Generated by Django 2.1.7 on 2019-04-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20190417_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrecipientlist',
            name='user',
            field=models.ManyToManyField(blank=True, to='customer.CustomerProfile'),
        ),
        migrations.AlterField(
            model_name='staffrecipientlist',
            name='user',
            field=models.ManyToManyField(blank=True, to='staff.StaffProfile'),
        ),
    ]
