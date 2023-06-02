from server import create_app


app = create_app()

@app.route('/static/<path:path>')
def serve_static(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run()
