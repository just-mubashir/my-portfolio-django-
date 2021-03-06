# Generated by Django 4.0.4 on 2022-05-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='year_awarded',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='year_of_joining',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='year_of_passing',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiance',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experiance',
            name='start_date',
            field=models.DateField(),
        ),
    ]
