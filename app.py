from flask import Flask, render_template, request, send_file

import numpy as np
import scipy.signal as sps
# File: games/jump.py
from flask import Blueprint, render_template, request, send_file
import numpy as np
import scipy.signal as sps

from games.jump import jump_blueprint
from games.redgreen import red_blueprint

# Specify a different template folder for the jump blueprint
app = Flask(__name__, template_folder='templates')
app.register_blueprint(jump_blueprint, url_prefix='/jump')
app.register_blueprint(red_blueprint, url_prefix='/redgreen')



def index():
    return render_template('mainpage.html')






@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

@app.route('/playpage')
def playpage():
    return render_template('playpage.html')


@app.route('/createloby')
def createloby():
    return render_template('create_loby.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
