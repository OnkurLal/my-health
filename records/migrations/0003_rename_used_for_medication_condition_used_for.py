# Generated by Django 4.2.4 on 2023-08-31 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_doctor_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medication',
            old_name='used_for',
            new_name='condition_used_for',
        ),
    ]