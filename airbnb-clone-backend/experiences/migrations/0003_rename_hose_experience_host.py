# Generated by Django 4.1.2 on 2022-11-02 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0002_experience_category_alter_perk_details_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="experience",
            old_name="hose",
            new_name="host",
        ),
    ]