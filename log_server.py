import os
from flask import Flask, render_template, abort

app = Flask(__name__)

LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')

@app.route('/')
def index():
    files = [f for f in os.listdir(LOG_DIR) if f.endswith('.txt')]
    return render_template('index.html', files=files)

@app.route('/logs/<path:filename>')
def view_log(filename):
    file_path = os.path.join(LOG_DIR, filename)
    if not os.path.isfile(file_path):
        abort(404)
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    return render_template('view.html', filename=filename, content=content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
