# Generated by Django 2.1.7 on 2019-02-27 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='time_received',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
