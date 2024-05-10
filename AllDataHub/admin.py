from django.contrib import admin

# Register your models here.
from AllDataHub.models import DiseaseDetails, HospitalHub

admin.site.register(DiseaseDetails)
admin.site.register(HospitalHub)
