import requests
from config import CLIENT_ID, CLIENT_SECRET, FAA_API_URL
import json
from objects.Notam import Notam  # Import Notam Class
from objects.Coordinate import Coordinate
import concurrent.futures
import threading
import time
from ratelimit import limits, sleep_and_retry
class NotamFetcher:
    def __init__(self):
        self.headers = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        self.response_format = 'geoJson'
        self.lock = threading.Lock()

    def fetch_by_coordinates(self, coordinates, radius=10):
        notams = set()
        start_time = time.time()
        def process_coordinate(coordinate):
            result = self.fetch_notams_with_retry(coordinate, radius)
            total_pages = result['totalPages']
            current_page = result['pageNum']
            
            with self.lock:
                notams.update([Notam(json.dumps(item)) for item in result['items']])
            
            while current_page < total_pages:
                current_page += 1
                result = self.fetch_notams_with_retry(coordinate, radius, current_page)
                
                with self.lock:
                    notams.update([Notam(json.dumps(item)) for item in result['items']])

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            for i in range(0, len(coordinates), 10):
                batch = coordinates[i:i+10]
                futures = [executor.submit(process_coordinate, coord) for coord in batch]
                concurrent.futures.wait(futures)
                time.sleep(2)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return list(notams)

    @sleep_and_retry
    @limits(calls=1, period=1)  # Limit to 1 call per second
    def fetch_notams_with_retry(self, coordinate, radius, page_number=1, max_retries=5):
        for attempt in range(max_retries):
            try:
                return self.fetch_notams(coordinate, radius, page_number)
            except requests.exceptions.RequestException as e:
                if e.response is not None and e.response.status_code == 429:
                    retry_after = int(e.response.headers.get('Retry-After', 5))
                    print(f"Rate limit exceeded. Retrying after {retry_after} seconds.")
                    time.sleep(retry_after)
                elif attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"Request failed. Retrying in {wait_time} seconds.")
                    time.sleep(wait_time)
                else:
                    raise
    
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

