from django.db import models

# Create your models here.

class Disease(models.Model):
    disease = models.CharField(max_length=255)
    symptoms = models.CharField(max_length=255)
    treatments = models.CharField(max_length=255)
    medications = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.disease
    