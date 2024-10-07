from flask import Flask, jsonify
from flask_cors import CORS

from utilities.GeoUtilities import GeoUtilities
from utilities.NotamFetcher import NotamFetcher
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
    GeoUtils = GeoUtilities()

    airport_a_coor = GeoUtils.geo_resolve(airport_a)
    airport_b_coor = GeoUtils.geo_resolve(airport_b)
    flightpath_coords = GeoUtils.build_flight_path(airport_a_coor, airport_b_coor)
    
    # Request Notams. For now, this returns a string instead of a list of NOTAMs.
    notamFetcher = NotamFetcher()

    notams = notamFetcher.fetch_by_coordinate(flightpath_coords)
    
    
    ## Under Construction

    # Delete repeated Notams
    # NotamUtils.delete_repeated_notams(notams)
    
    # Sort Notams. "X" here can be replaced by any implementing class of NotamSorter, e.g., DummySorter
    # notams = XSorter.sort(Notams)
    
    
    # Prep for Display
    # displayString = ""
    # for ( Notam notam : notams)
    #     displayString.add( notam.jsonify_notam())

        
    return jsonify(notams)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
