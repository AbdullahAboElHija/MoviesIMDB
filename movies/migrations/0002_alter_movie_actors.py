# Generated by Django 5.1.1 on 2024-09-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.TextField(max_length=200),
        ),
    ]
