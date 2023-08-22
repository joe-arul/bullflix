# if port 5000 in use already, try: export [FLASK_RUN_PORT=8080] before [flask run]
from flask import Flask, render_template

from flask import Flask, request, jsonify
# import cx_Oracle

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text


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

# Flask route to render User Details Page

@app.route('/userdetails')
def userdetails():
    return render_template('userdetails.html')


# Replace these values with your actual Oracle database credentials
#db_config = {
#    'user': 'JOEARUL',
#    'password': 'usf1956!',
#    'dsn': 'reade.forest.usf.edu:1521/cdb9'  # Example: 'localhost/XE'
#}


# Replace these values with your actual Oracle database credentials
db_config = {
    'user': 'JOEARUL',
    'password': 'usf1956!',
    'host': 'reade.forest.usf.edu:',
    'port': '1521',
    'service_name': 'cdb9'
}

# Create the SQLAlchemy engine
connection_string = f"oracle+cx_oracle://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['service_name']}"
engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Define a function to connect to the Oracle database
#def connect_db():
#    return cx_Oracle.connect(user=db_config['user'], password=db_config['password'], dsn=db_config['dsn'])

# Define a route to handle form submission
@app.route('/search', methods=['POST'])
def search():
    email = request.form['email']

    # Query the database
#    query = "SELECT * FROM your_table_name WHERE email = :email"
#    conn = connect_db()
#    cursor = conn.cursor()
#    cursor.execute(query, {'email': email})

    query = text("SELECT * FROM your_table_name WHERE email = :email")
    results = engine.execute(query, email=email).fetchall()
#    results = cursor.fetchall()
#    cursor.close()
#    conn.close()

    # Prepare the HTML response
    if len(results) > 0:
        results_html = "<h3>Search Results:</h3><ul>"
        for result in results:
            results_html += f"<li>Email: {result[0]}</li>"
        results_html += "</ul>"
    else:
        results_html = "<p>No matching records found.</p>"

    return f"{results_html}"

    #return jsonify(results)

