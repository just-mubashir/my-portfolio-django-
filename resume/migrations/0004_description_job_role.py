# Generated by Django 4.0.4 on 2022-05-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_education_city_education_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='job_role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
