from django.test import TestCase
import requests

def find_hospitals_nearby(location, disease, access_token):
    radius = 10000  # Specify the radius within which to search for hospitals, in meters
    
    # Construct the API request URL
    url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?access_token={access_token}&types=hospital&limit=10'
    
    # Send the HTTP request to the Mapbox Geocoding API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if any hospitals were found
        if 'features' in data:
            hospitals = data['features']
            return hospitals
        else:
            return None
    else:
        print("Error:", response.status_code)
        return None

# Example usage:

location = 'RGIPT Jais,Amethi'  # Example: 'San Francisco, CA'
disease = 'Fungal Infection'  # Example: 'COVID-19'
access_token = 'pk.eyJ1IjoiYWJoaXNoZWtoOTkiLCJhIjoiY2xsd3E3MzQ5MHZqODNkbWRqYmE1amdzdyJ9.WsiriAY-8cDL7TLfPJjp2A'  # Replace 'YOUR_MAPBOX_ACCESS_TOKEN' with your actual access token

hospitals = find_hospitals_nearby(location, disease, access_token)
if hospitals:
    print("Hospitals nearby:")
    for hospital in hospitals:
        print(hospital['place_name'])
else:
    print("No hospitals found nearby.")


