from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename

from server.api.service.image_service import get_images_data, process_image


api_v1 = Blueprint('api_v1', __name__)

@api_v1.route('/api/v1/sanity', methods=['GET'])
def sanity():
    return jsonify('check!')

@api_v1.route('/api/v1/dataframe', methods=['GET'])
def dataframe():
    data = get_images_data()
    return jsonify(data)

@api_v1.route('/api/v1/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    file.filename = secure_filename(file.filename)

    data = process_image(file)

    return jsonify(data), 200
