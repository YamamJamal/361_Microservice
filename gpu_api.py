from flask import Flask, jsonify, redirect
import json

app = Flask(__name__)

# Load GPU data from the JSON file
with open('gpu_data.json') as file:
    gpu_data = json.load(file)


@app.route('/', methods=['GET'])
def index():
    return redirect('/api/gpu')


@app.route('/api/gpu', methods=['GET'])
def get_gpu_data():
    return jsonify(gpu_data)


if __name__ == '__main__':
    app.run()
