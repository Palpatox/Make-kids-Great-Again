# File: games/jump.py
from flask import Blueprint, render_template, request, send_file
import numpy as np
import scipy.signal as sps

jump_blueprint = Blueprint('jump', __name__, template_folder='custom_templates')

# Initialize a dictionary to store accelerometer data for each client
client_data_dict = {}

client_role_dict = {}

jump_results = {}
# Initialize an array of available roles
available_roles = ['Player1', 'Player2','Player3','Player4','Player5']

@jump_blueprint.route('/')
def jump_index():
    return render_template('jump.html')

@jump_blueprint.route('/reset_jump', methods=['POST'])
def reset_jump():
    print('restarted')
    client_ip = request.remote_addr
    client_data_dict[client_ip] = np.array([])

@jump_blueprint.route('/get_result', methods=['GET'])
def get_result():
    global client_data_dict
    '''function receives an np.array as an input and returns count,
    requires import numpy as np, import scipy.signal as sps'''
    count={}
    # cleaning the array from Nones
    for key in client_data_dict:
        accelerationY=client_data_dict[key]
        arr = accelerationY[accelerationY != np.array(None)]
    
    # min-max normalization
        xmax = arr.max()
        xmin = arr.min()
        arr = (arr - xmin) / (xmax - xmin)
    
    # counting the peaks (! basic consideration: refreshing rate = 100 Hertz, thus distance=30 is 0.3 seconds)
        count[key] = len(sps.find_peaks(arr, height=0.6, distance=30)[0])
        print(client_role_dict[key])
        jump_results[client_role_dict[key]]= len(sps.find_peaks(arr, height=0.6, distance=30)[0])

    return jump_results

@jump_blueprint.route('/accelerometer', methods=['POST'])
def accelerometer():
    data = request.json
    client_ip = request.remote_addr
    # print("Accelerometer data received:", data['accelerationIncludingGravity']['y'], client_ip)

    # Check if the client already has an array, if not, initialize one
    if client_ip not in client_data_dict:
        client_data_dict[client_ip] = np.array([])

    # Add the received data to the client's array
    client_data_dict[client_ip] = np.append(client_data_dict[client_ip], data['acceleration']['y'])

    # filename = f'save_{client_ip}.npy'
    # np.save(filename, client_data_dict[client_ip])

    return 'OK'

@jump_blueprint.route('/assign_role', methods=['GET'])
def assign_role():
    client_ip = request.remote_addr

    if client_ip not in client_role_dict:
        if available_roles:
            assigned_role = available_roles.pop(0)
            print('inside roler', assigned_role)
            client_role_dict[client_ip]=assigned_role
            
            return f'Your role: {assigned_role}'
    else:
        return f'Your role: {client_role_dict[client_ip]}'

    return 'OK'
