from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import csv
from django.shortcuts import HttpResponse
from .models import HospitalHub



def import_hospitals_from_csv(request):
    # Path to your CSV file
    csv_file_path = r'C:\Users\Abhishek Yadav\OneDrive - rgipt.ac.in\Desktop\DiseasePrediction\dataset\HospitalDetails.csv'
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                HospitalHub.objects.create(
                    disease=row['Disease'],
                    hospital_name=row['Hospital Name'],
                    location=row['Location'],
                    contact_information=row['Contact Information'],
                    specialties=row['Specialties'],
                    doctors_and_specialists=row['Doctors and Specialists'],
                    treatment_options=row['Treatment Options'],
                    facilities_and_amenities=row['Facilities and Amenities']
                )
        return HttpResponse("Hospital data imported successfully")
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
