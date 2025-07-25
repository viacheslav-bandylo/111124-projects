# Generated by Django 5.2.3 on 2025-07-24 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_order_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "get_latest_by": "order_date",
                "ordering": ["-order_date"],
                "permissions": [
                    ("can_view_order_statistics", "Can view order statistics")
                ],
            },
        ),
    ]
