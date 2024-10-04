import requests

from config import CLIENT_ID, CLIENT_SECRET, FAA_API_URL
from objects.Coordinate import Coordinate

class NotamFetcher:
    def __init__(self):
        self.headers = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
        }

        self.response_format='geoJson'

    def fetch_by_coordinate(self, coordinates, radius = 10):
        # Returns notams based on an array of coordinates and a radius. For now, returns a string instead of a list of notams.
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
                print("Response Text:", response.text)

                response.raise_for_status()
                data = response.json()
                current_notam_list = [item['properties']['coreNOTAMData']['notam'] for item in data['items']]
                notams.extend(current_notam_list)

            except requests.exceptions.RequestException as e:
                print(f"An error occurred while fetching NOTAMs: {e}")
                raise e
            
        return notams
