# Generated by Django 5.2.3 on 2025-07-17 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TaskManager", "0037_alter_subtask_deadline_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subtask",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 7, 18, 10, 5, 54, 812849, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 7, 18, 10, 5, 54, 812849, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
