# Generated by Django 2.1.7 on 2019-04-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_appointment_rejected_requested_cancellation'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField(default=1)),
                ('last_minute_cancellation_time', models.IntegerField(default=3)),
            ],
        ),
    ]
