from django.db import models

# Create your models here.
class Patient(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.username} {self.name}'
    
class PastRecords(models.Model):

    username = models.CharField(max_length=100)
    disease = models.CharField(max_length=200)
    discription = models.TextField()
    symptoms = models.TextField()
    precautions = models.TextField()
    medication = models.TextField()
    date = models.DateField(auto_created=True, auto_now=True)
    def __str__(self):
        return f'{self.username} {self.disease}'
    

