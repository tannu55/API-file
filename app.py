from flask import Flask, request, jsonify
from logic import compute_min_cost

app = Flask(__name__)

@app.route('/')
def home():
    return "Delivery Cost API is running!"

@app.route('/calculate_cost', methods=['POST'])
def calculate_cost():
    try:
        order = request.get_json()
        if not order:
            return jsonify({'error': 'No JSON body found'}), 400

        cost = compute_min_cost(order)
        return jsonify({'minimum_cost': cost})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
