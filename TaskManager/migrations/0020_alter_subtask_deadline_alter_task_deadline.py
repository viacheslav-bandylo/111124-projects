# Generated by Django 5.2.3 on 2025-06-23 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0019_alter_subtask_deadline_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 24, 18, 35, 35, 591032, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 24, 18, 35, 35, 591032, tzinfo=datetime.timezone.utc)),
        ),
    ]
