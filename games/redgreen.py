# File: games/jump.py
from flask import Blueprint, render_template, request, send_file
import numpy as np
import scipy.signal as sps

red_blueprint = Blueprint('redgreen', __name__, template_folder='custom_templates')


@red_blueprint.route('/')
def redgreen():
    return render_template('redgreen.html')