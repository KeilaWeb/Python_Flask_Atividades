import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('artigos.json', 'r') as f:
        artigos = json.load(f)
    return render_template('index.html', artigos = artigos)

if __name__ == '__main__':
    app.run(debug=True)