# Generated by Django 5.2.3 on 2025-06-23 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0009_alter_subtask_deadline_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 24, 15, 38, 1, 861640, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 24, 15, 38, 1, 861640, tzinfo=datetime.timezone.utc)),
        ),
    ]
