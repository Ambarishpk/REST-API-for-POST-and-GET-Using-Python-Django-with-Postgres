# Generated by Django 3.0.2 on 2020-01-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='age',
            field=models.CharField(max_length=2),
        ),
    ]
