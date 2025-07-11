import requests
import os
from dotenv import load_dotenv
load_dotenv()

ORS_API_KEY = os.environ.get('ORS_API_KEY', 'eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjVmYTEwOTE1YjUwZjRiNzhiOThhYTMxZGU2NWM4ZGY4IiwiaCI6Im11cm11cjY0In0=')

def get_route(coords):
    url = "https://api.openrouteservice.org/v2/directions/driving-car/geojson"
    headers = {
        'Authorization': ORS_API_KEY,
        'Content-Type': 'application/json'
    }
    body = {
        "coordinates": coords
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code, response.text)  # Add this line for debugging
    if response.status_code == 200:
        return response.json()
    else:
        return None