import os
import base64

BASE_URL = 'http://localhost:5001'

def get_images_data():
    images_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'static', 'data', 'poster')

    data = []

    for filename in os.listdir(images_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            data.append({
                'rank': int(os.path.splitext(filename)[0]) + 1,
                'url': f'{BASE_URL}/static/data/poster/{filename}',
                'kpis': [
                    {'code': 'genre', 'value': ['Action', 'Adventure']},
                    {'code': 'main_title', 'value': ['tittle']},
                    {'code': 'main_color', 'value': ['blue']},
                    {'code': 'main_text_color', 'value': ['white']},
                    {'code': 'main_text_position', 'value': ['mid-bottom', 'center']},
                    {'code': 'main_text_size', 'value': ['big']},
                    {'code': 'face_number', 'value': ['3']},
                ],
            })

    # Sort by rank
    data.sort(key=lambda item: item['rank'])

    return data

def process_image(file):
    # TODO: process image with ia tools

    content = base64.b64encode(file.read()).decode()
    data = {
        'file': content,
        'name': file.filename,
        'kpis': [
            {'code': 'genre', 'value': ['Drama', 'Crime', 'Mystery']},
            {'code': 'main_title', 'value': ['The Shawshank Redemption']},
            {'code': 'main_color', 'value': ['black']},
            {'code': 'main_text_color', 'value': ['white']},
            {'code': 'main_text_position', 'value': ['bottom', 'center']},
            {'code': 'main_text_size', 'value': ['big']},
            {'code': 'face_number', 'value': ['1']},
        ]
    }

    return data


    # "avg_red": 60.543148148148134,
    # "avg_green": 79.77301080246917,
    # "avg_blue": 103.38674691358032,
    # "has_face": true,
    # "num_faces": 2.0,
    # "has_text_top_quarter": 0.0,
    # "has_face_center": true,
    # "has_text_bottom_half": 1.0,
    # "num_text_lines_bottom_quarter": 8.0,
    # "largest_text_percentage": 100.0,
    # "dominant_color": "Black",
    # "is_text_in_bottom_quarter": 1.0,
    # "num_distinct_colors": 99486.0