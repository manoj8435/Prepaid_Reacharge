# Generated by Django 4.1.4 on 2022-12-11 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recharge", "0002_areacircle_categoryplan_operator_plan_recharge"),
    ]

    operations = [
        migrations.RenameField(
            model_name="areacircle",
            old_name="area",
            new_name="area_name",
        ),
    ]