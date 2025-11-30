from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/index')
def index_page():
    return render_template('index.html')

@app.route('/munroe')
def munroe_page():
    return render_template('Munroe.html')

@app.route('/mona')
def mona_page():
    return render_template('Mona.html')

if __name__ == '__main__':
    app.run(debug=True)