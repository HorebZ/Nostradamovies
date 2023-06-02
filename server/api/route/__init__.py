from flask import Blueprint, jsonify

from server.api.service.image_service import get_image_urls


api_v1 = Blueprint('api_v1', __name__)

@api_v1.route('/api/v1/sanity', methods=['GET'])
def sanity():
    return jsonify('check!')

@api_v1.route('/api/v1/images', methods=['GET'])
def images():
    image_urls = get_image_urls()
    return jsonify(image_urls)
