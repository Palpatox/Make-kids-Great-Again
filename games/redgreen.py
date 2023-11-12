# Import necessary modules from Flask for web application development
from flask import Blueprint, render_template, request, send_file
import numpy as np
import scipy.signal as sps

# Create a Blueprint instance for the 'redgreen' game module
red_blueprint = Blueprint('redgreen', __name__, template_folder='custom_templates')

# Define a route that renders the main page for the 'redgreen' game module
@red_blueprint.route('/')
def redgreen():
    return render_template('redgreen.html')
