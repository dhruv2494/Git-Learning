from flask import Flask, jsonify
import json


app = Flask(__name__)


data_file = 'data.json'


def read_data_from_file():
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


@app.route('/api', methods=['GET'])
def api():
    data = read_data_from_file()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)