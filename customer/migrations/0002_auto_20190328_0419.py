# Generated by Django 2.1.7 on 2019-03-28 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_type',
            field=models.CharField(max_length=15),
        ),
    ]
