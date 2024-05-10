# Generated by Django 4.2.6 on 2024-04-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=200)),
                ('disease_description', models.TextField()),
                ('disease_symptoms', models.TextField()),
                ('disease_prevention', models.TextField()),
                ('disease_treatment', models.TextField()),
                ('disease_medications', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HospitalHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=100)),
                ('hospital_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact_information', models.CharField(max_length=100)),
                ('specialties', models.TextField()),
                ('doctors_and_specialists', models.TextField()),
                ('treatment_options', models.TextField()),
                ('facilities_and_amenities', models.TextField()),
            ],
        ),
    ]