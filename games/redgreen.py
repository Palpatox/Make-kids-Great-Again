# Import necessary modules application development
from flask import Blueprint, render_template, request, send_file
import numpy as np
import scipy.signal as sps

# Create a Blueprint instance for 'Red light Green light' game 
red_blueprint = Blueprint('redgreen', __name__, template_folder='custom_templates')

# Define a route that renders the main page for the 'Red light Green light' game
@red_blueprint.route('/')
def redgreen():
    return render_template('redgreen.html')
