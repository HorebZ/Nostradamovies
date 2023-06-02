import os

BASE_URL = 'http://localhost:5001'

def get_image_urls():
    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'static', 'data', 'poster')

    images = []

    for filename in os.listdir(images_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            images.append(filename)

    # Sort by numeric order
    images.sort(key=lambda x: int(os.path.splitext(x)[0]))

    image_urls = [f'{BASE_URL}/static/data/poster/{image}' for image in images]

    return image_urls