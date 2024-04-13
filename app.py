from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def handle_data():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"status": "Data received"}), 200

if __name__ == '__main__':
    app.run(debug=True)
