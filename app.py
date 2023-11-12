# Import necessary modules for application development
from flask import Flask, render_template, request, send_file
import numpy as np
import scipy.signal as sps

# Import blueprints for game modules
from games.jump import jump_blueprint
from games.redgreen import red_blueprint

# Create a Flask application instance
app = Flask(__name__, template_folder='templates')

# Register blueprints for different game modules with specified URL prefixes
app.register_blueprint(jump_blueprint, url_prefix='/jump')
app.register_blueprint(red_blueprint, url_prefix='/redgreen')

# Define the default route that renders the main page
def index():
    return render_template('mainpage.html')

# Define a route for the main page
@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

# Define a route for the play page
@app.route('/playpage')
def playpage():
    return render_template('playpage.html')

# Define a route for creating a lobby
@app.route('/createloby')
def createloby():
    return render_template('create_loby.html')

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
