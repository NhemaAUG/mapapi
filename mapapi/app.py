from flask import Flask, render_template, jsonify, request
from templates.routing import get_route

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/route', methods=['POST'])
def api_route():
    data = request.get_json()
    print("Received coordinates:",data)
    coords = data.get('coordinates')
    route = get_route(coords)
    print("Route result:",route)
    if route:
        return jsonify(route)
    else:
        return jsonify({'error': 'Could not get route'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)