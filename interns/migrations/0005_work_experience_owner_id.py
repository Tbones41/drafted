# Generated by Django 4.1.4 on 2022-12-16 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("interns", "0004_alter_education_level_of_edu_alter_education_grade_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="work_experience",
            name="owner_id",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="interns.profile",
            ),
        ),
    ]