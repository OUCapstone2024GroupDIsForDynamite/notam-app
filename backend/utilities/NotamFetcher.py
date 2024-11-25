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

    def fetch_by_coordinates(self, coordinates, radius=40):
        # Returns notams as Notam objects based on an array of coordinates and a radius
        notams = set()

        for coordinate in coordinates:
            result = self.fetch_notams(coordinate, radius)

            total_pages = result['totalPages']
            current_page = result['pageNum']

            # Convert result to Notam objects
            notams.update( [ Notam( json.dumps(item) ) for item in result['items']  ] )

            while (current_page < total_pages):
                current_page += 1
                result = self.fetch_notams(coordinate, radius, current_page)

                notams.update( [ Notam( json.dumps(item) ) for item in result['items']  ] )


        return list(notams)
    
    # Call API with given parameters
    def fetch_notams(self, coordinate, radius, page_number= 1):
        
        params = {
                    'responseFormat': self.response_format,
                    'locationLatitude': coordinate.latitude,
                    'locationLongitude': coordinate.longitude,
                    'locationRadius': radius,
                    'pageSize' : 500,
                    'pageNum' : page_number
                }

        try:
            response = requests.get(f"{FAA_API_URL}/notams", headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()

            print(f"Fetched {len(data['items'])} notam(s) at ({coordinate.latitude}, {coordinate.longitude}) on page {page_number}/{data['totalPages']}")

            return data
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching NOTAMs: {e}")
            raise e

