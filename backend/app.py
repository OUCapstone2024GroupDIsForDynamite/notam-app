from flask import Flask, jsonify
from flask_cors import CORS

from utilities.GeoUtilities import GeoUtilities
from utilities.NotamFetcher import NotamFetcher
from utilities.DummySorter import DummySorter
from objects.Coordinate import Coordinate

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config')))


app = Flask(__name__)

CORS(app)

# Existing endpoint
@app.route('/api/notams', methods=['GET'])
def get_notams():
    response = jsonify({'msg': 'NOTAM'})
    return response

# New endpoint to generate a flight briefing based on two airport codes
@app.route('/api/notam/<airport_a>/<airport_b>', methods=['GET'])
def generate_flight_briefing(airport_a, airport_b):
    # Get querying coordinates
    geo_utils = GeoUtilities()

    airport_a_coor = geo_utils.geo_resolve(airport_a)
    airport_b_coor = geo_utils.geo_resolve(airport_b)
    flightpath_coords = geo_utils.build_flight_path(airport_a_coor, airport_b_coor)

    # Request Notams
    notam_fetcher = NotamFetcher()
    notams = notam_fetcher.fetch_by_coordinates(flightpath_coords)
    
    # Sort Notams. "Dummy" can be replaced by any implementing class of NotamSorter
    notams = DummySorter().sort(notams)
    

    # Convert Notam objects to dictionaries for JSON serialization
    notam_list = [notam.jsonify_notam() for notam in notams]

    return jsonify(notam_list)  # Return the list of dictionaries as a JSON response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
