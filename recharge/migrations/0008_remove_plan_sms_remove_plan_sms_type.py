# Generated by Django 4.1.4 on 2022-12-11 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recharge", "0007_plan_validity_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plan",
            name="sms",
        ),
        migrations.RemoveField(
            model_name="plan",
            name="sms_type",
        ),
    ]