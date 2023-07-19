# if port 5000 in use already, try: export [FLASK_RUN_PORT=8080] before [flask run]
from flask import Flask, render_template

app = Flask(__name__)

# Flask route to render homepage

@app.route("/")
def home():
    return render_template('index.html')

# Flask route to render About Us page

@app.route('/about')
def about():
    return render_template('about.html')

# Flask route to render Movie List page

@app.route("/movies")
def features():
    return render_template('movies.html')

# Flask route to render Categories Page

@app.route('/categories')
def signup():
    return render_template('categories.html')





