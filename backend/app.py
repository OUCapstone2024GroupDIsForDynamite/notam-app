from flask import Flask, jsonify
from flask_cors import CORS

import sys
import os
import requests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config')))

from config import CLIENT_ID, CLIENT_SECRET, BASE_URL


app = Flask(__name__)

CORS(app)

# Existing endpoint
@app.route('/api/notams', methods=['GET'])
def get_notams():
    response = jsonify({'msg': 'NOTAM'})
    return response

# New endpoint to return specific airport location data based on its ICAO_location
@app.route('/api/notam/<location>', methods=['GET'])
def get_notam(location):
    notam = fetch_notam(location)
    if notam:
        response = jsonify(notam)
    else:
        response = jsonify({'error': 'NOTAM not found'}), 404
    return response


def fetch_notam(icao_location, response_format='geoJson'):

    headers = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    params = {
        'icaoLocation': icao_location,
        'responseFormat': response_format
    }    

    try:
        response = requests.get(f"{BASE_URL}/notams", headers=headers, params=params)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text[:500])

        response.raise_for_status()
        data = response.json()
        notam_list = [item['properties']['coreNOTAMData']['notam'] for item in data['items']]
        return notam_list

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching NOTAMs: {e}")
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
