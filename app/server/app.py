import os

from flask import Flask, render_template

from utils.tailwind import Watcher as TailwindWatcher

# app
app = Flask(__name__)

# ressources
img = os.path.join('static', 'img')
svg = os.path.join('static', 'svg')

# routes
@app.route("/")
@app.route("/index")
def index():
    background = os.path.join(img, 'header.jpg')

    return render_template("index.html", background=background)


if __name__ == '__main__':
    # Run TailwindCSS as subprocess; watch for changes; build css on-the-fly
    TailwindWatcher(root_path=app.root_path, npm_script_name="watch")
    app.run(debug=True)

