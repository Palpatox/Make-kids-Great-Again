# Import necessary modules from Flask for web application development
from flask import Blueprint, render_template, request, send_file
import numpy as np
import scipy.signal as sps

# Create a Blueprint instance for the 'Rope Jumping' game
jump_blueprint = Blueprint('jump', __name__, template_folder='custom_templates')

# Initialize dictionaries and arrays to store game-related data
client_data_dict = {}    # Dictionary to store accelerometer data for each client
client_role_dict = {}    # Dictionary to store assigned roles for each client
jump_results = {}        # Dictionary to store jump results for each role
available_roles = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5']  # Array of available roles

# Define a route that renders the main page for the 'jump' game module
@jump_blueprint.route('/')
def jump_index():
    return render_template('jump.html')

# Define a route that resets the 'jump' game state
@jump_blueprint.route('/reset_jump', methods=['POST'])
def reset_jump():
    print('restarted')
    client_ip = request.remote_addr
    client_data_dict[client_ip] = np.array([])

# Define a route that returns jump results based on accelerometer data
@jump_blueprint.route('/get_result', methods=['GET'])
def get_result():
    global client_data_dict
    
    # Count number of jumpes by detecting peaks in accelerometer data
    count = {}
    for key in client_data_dict:
        accelerationY = client_data_dict[key]
        arr = accelerationY[accelerationY != np.array(None)]
        xmax = arr.max()
        xmin = arr.min()
        arr = (arr - xmin) / (xmax - xmin)
        count[key] = len(sps.find_peaks(arr, height=0.6, distance=30)[0])
        print(client_role_dict[key])
        jump_results[client_role_dict[key]] = len(sps.find_peaks(arr, height=0.6, distance=30)[0])

    return jump_results

# Define a route that receives accelerometer data from clients
@jump_blueprint.route('/accelerometer', methods=['POST'])
def accelerometer():
    data = request.json
    client_ip = request.remote_addr
    
    # Check if the client already has an array, if not, initialize one
    if client_ip not in client_data_dict:
        client_data_dict[client_ip] = np.array([])

    # Add the received accelerometer data to the client's array
    client_data_dict[client_ip] = np.append(client_data_dict[client_ip], data['acceleration']['y'])
    
    return 'OK'

# Define a route that assigns roles to clients
@jump_blueprint.route('/assign_role', methods=['GET'])
def assign_role():
    client_ip = request.remote_addr

    # Check if the client already has a role assigned, if not, assign one
    if client_ip not in client_role_dict:
        if available_roles:
            assigned_role = available_roles.pop(0)
            print('inside roler', assigned_role)
            client_role_dict[client_ip] = assigned_role
            return f'Your role: {assigned_role}'
    else:
        return f'Your role: {client_role_dict[client_ip]}'

    return 'OK'
