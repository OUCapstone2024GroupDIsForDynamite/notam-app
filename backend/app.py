from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/notams')
def get_notams():
    # return 'notam'
    response = jsonify({'msg': 'NOTAM'})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
