# Generated by Django 4.1.4 on 2022-12-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interns", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile", name="age", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="referee", name="number", field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="user", name="phone", field=models.BigIntegerField(),
        ),
    ]