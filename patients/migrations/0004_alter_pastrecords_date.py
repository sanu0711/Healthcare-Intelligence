# Generated by Django 4.2.6 on 2024-04-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_alter_pastrecords_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastrecords',
            name='date',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
    ]
