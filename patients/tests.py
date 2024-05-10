# from django.test import TestCase

# Create your tests here.
from patients.models import Patient, PastRecords
data=PastRecords.objects.all()
print(data)