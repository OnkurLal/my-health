# Generated by Django 4.2.4 on 2023-09-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctors", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="zip_code",
            field=models.CharField(max_length=5, null=True),
        ),
    ]