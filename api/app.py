import os

from flask import Flask, jsonify, request
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# static ressources
app = Flask(__name__, static_folder='../data/dataset/top1000/data/')

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# routes
@app.route('/api/v1/sanity', methods=['GET'])
def sanity():
    return jsonify('check!')

@app.route('/api/v1/images', methods=['GET'])
def images():
    images_path = '../data/dataset/top1000/data/'
    images = []

    for filename in os.listdir(images_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(filename)

    # sorte by numeric order
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))

    base_url = request.host_url.rstrip('/')
    image_urls = [f'{base_url}/static/{image}' for image in images]

    return jsonify(image_urls)

@app.route('/static/<path:path>')
def serve_static(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run()