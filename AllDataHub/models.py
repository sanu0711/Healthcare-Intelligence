from django.db import models

# Create your models here.

class DiseaseDetails(models.Model):

    disease_name = models.CharField(max_length=200, unique=True)
    disease_description = models.TextField()
    disease_symptoms = models.TextField()
    disease_precaution = models.TextField()
    disease_medications = models.TextField()
    def __str__(self):
        return self.disease_name
    
class HospitalHub(models.Model):
    disease_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    specialties = models.TextField()
    doctors_and_specialists = models.TextField()
    treatment_options = models.TextField()
    facilities_and_amenities = models.TextField()

    def __str__(self):
        return self.hospital_name

