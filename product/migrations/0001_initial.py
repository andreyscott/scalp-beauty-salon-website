# Generated by Django 2.1.7 on 2019-03-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('gender', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(default='default.jpeg', upload_to='images/products/')),
            ],
        ),
    ]
