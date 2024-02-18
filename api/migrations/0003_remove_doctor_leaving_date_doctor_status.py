# Generated by Django 5.0.2 on 2024-02-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_alter_doctor_leaving_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="leaving_date",
        ),
        migrations.AddField(
            model_name="doctor",
            name="status",
            field=models.CharField(
                choices=[("Active", "Active"), ("Inactive", "Inactive")],
                default="Active",
                max_length=20,
            ),
        ),
    ]
