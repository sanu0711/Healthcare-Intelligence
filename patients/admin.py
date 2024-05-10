from django.contrib import admin

# Register your models here.

from .models import Patient, PastRecords

admin.site.register(Patient)
admin.site.register(PastRecords)



