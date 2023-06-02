import os

from flask import Flask, render_template
from flask_cors import CORS

from utils.tailwind import Watcher as TailwindWatcher

# app
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# ressources
img = os.path.join('static', 'img')
svg = os.path.join('static', 'svg')

# routes
# sanity check route
@app.route('/api/v1/sanity', methods=['GET'])
def ping_pong():
    return jsonify('check!')

@app.route("/api/v1/images")
def get_images():
    images_folder = '../../data/

@app.route("/")
@app.route("/index")
def index():
    background = os.path.join(img, 'header.jpg')
    if not os.path.exists(background):
        background = None
    return render_template("index.html", background=background)


if __name__ == '__main__':
    # Run TailwindCSS as subprocess; watch for changes; build css on-the-fly
    TailwindWatcher(root_path=app.root_path, npm_script_name="watch")
    app.run(debug=True)
