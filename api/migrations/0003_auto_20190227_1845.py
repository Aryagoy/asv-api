# Generated by Django 2.1.7 on 2019-02-27 18:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190207_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=200)),
                ('msg_type', models.CharField(max_length=200)),
                ('receiver', models.CharField(max_length=200)),
                ('frequency', models.FloatField()),
                ('time_received', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Api',
        ),
    ]
