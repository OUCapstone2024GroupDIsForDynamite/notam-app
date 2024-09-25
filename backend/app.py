from flask import Flask, jsonify, request

app = Flask(__name__)

# Apply common headers to all responses
@app.after_request
def apply_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# Existing endpoint
@app.route('/api/notams', methods=['GET'])
def get_notams():
    response = jsonify({'msg': 'NOTAM'})
    return response

# New endpoint to return specific NOTAM data based on the number
@app.route('/api/notam/<notam_number>', methods=['GET'])
def get_notam(notam_number):
    # Check if the notam_number is None, empty string, or invalid
    if not notam_number or notam_number.strip() == '':
        return jsonify({'error': 'Invalid NOTAM number'}), 400

    mock_data = {
        '001': {
            'number': '001',
            'series': 'A',
            'id': '12345',
            'description': 'Runway 1 closed for maintenance.',
            'details': 'Runway 1 will be closed from 0100Z to 0600Z on 2024-09-20 for maintenance work.'
        },
        '002': {
            'number': '002',
            'series': 'B',
            'id': '67890',
            'description': 'Temporary airspace restriction.',
            'details': 'A temporary airspace restriction is in effect from 0800Z to 1200Z on 2024-09-20 due to a VIP visit.'
        },
        '003': {
            'number': '003',
            'series': 'C',
            'id': '54321',
            'description': 'Fog expected.',
            'details': 'Fog is expected in the vicinity of the airport from 0500Z to 1000Z on 2024-09-20. Pilots should expect reduced visibility.'
        },
        '004': {
            'number': '004',
            'series': 'D',
            'id': '98765',
            'description': 'Bird activity reported.',
            'details': 'Bird activity reported in the vicinity of the airport. Pilots should exercise caution when landing and taking off.'
        },
        '005': {
            'number': '005',
            'series': 'E',
            'id': '11223',
            'description': 'Emergency procedures drill.',
            'details': 'An emergency procedures drill will be conducted at the airport from 1400Z to 1500Z on 2024-09-20. Expect increased emergency vehicle activity.'
        }
    }

    # Fetch the NOTAM data
    notam = mock_data.get(notam_number)
    if notam:
        response = jsonify(notam)
    else:
        return jsonify({'error': 'NOTAM not found'}), 404

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
