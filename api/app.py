from flask import Flask, jsonify
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# routes
@app.route('/sanity', methods=['GET'])
def sanity():
    return jsonify('check!')


if __name__ == '__main__':
    app.run()