# Generated by Django 4.0.4 on 2022-05-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_certification_year_awarded_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]