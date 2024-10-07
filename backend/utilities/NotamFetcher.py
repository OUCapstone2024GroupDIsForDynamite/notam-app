import requests
from config import CLIENT_ID, CLIENT_SECRET, FAA_API_URL
import json
from objects.Notam import Notam  # Import Notam Class
from objects.Coordinate import Coordinate

class NotamFetcher:
    def __init__(self):
        self.headers = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        self.response_format = 'geoJson'

    def fetch_by_coordinate(self, coordinates, radius=10):
        # Returns notams as Notam objects based on an array of coordinates and a radius
        notams = []

        for coordinate in coordinates:
            params = {
                'responseFormat': self.response_format,
                'locationLatitude': coordinate.latitude,
                'locationLongitude': coordinate.longitude,
                'locationRadius': radius
            }

            try:
                response = requests.get(f"{FAA_API_URL}/notams", headers=self.headers, params=params)
                print("Status Code:", response.status_code)
                response.raise_for_status()
                data = response.json()

                # Create Notam objects from the response data
                for item in data['items']:
                    notam_as_json = json.dumps(item)  # Convert the item to a JSON string
                    notams.append(Notam(notam_as_json))  # Add Notam Object to the list

            except requests.exceptions.RequestException as e:
                print(f"An error occurred while fetching NOTAMs: {e}")
                raise e

        return notams
