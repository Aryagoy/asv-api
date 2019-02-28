# Generated by Django 2.1.7 on 2019-02-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_horizon_accel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_angle', models.FloatField()),
                ('stop_angle', models.FloatField()),
                ('angle_increment', models.FloatField()),
                ('range_min', models.FloatField()),
                ('range_max', models.FloatField()),
                ('ranges', models.TextField()),
                ('intensities', models.TextField()),
            ],
        ),
    ]