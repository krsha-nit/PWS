from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for the API
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run()
