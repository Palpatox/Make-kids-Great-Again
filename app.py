from flask import Flask, render_template, request, send_file
import numpy as np

app = Flask(__name__, template_folder='templates', static_folder='templates')

# Initialize a dictionary to store accelerometer data for each client
client_data_dict = {}

client_role_dict = {}

jump_results = {}
# Initialize an array of available roles
available_roles = ['Player1', 'Player2','Player3','Player4','Player5']
@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/reset_jump', methods=['POST'])
def reset_jump():
    print('restartred')
    client_ip = request.remote_addr
    client_data_dict[client_ip] = np.array([])


@app.route('/get_result', methods=['GET'])
def get_result():
    global client_data_dict
    '''function receive an np.array as an input and returns count,
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

        # client_data_dict[key]=np.array([])
    # client_data_dict = {}
    
    return jump_results



@app.route('/accelerometer', methods=['POST'])
def accelerometer():
    data = request.json
    client_ip = request.remote_addr
    # print("Accelerometer data received:", data['accelerationIncludingGravity']['y'], client_ip)

    # Check if the client already has an array, if not, initialize one
    if client_ip not in client_data_dict:
        client_data_dict[client_ip] = np.array([])

    # Add the received data to the client's array
    client_data_dict[client_ip] = np.append(client_data_dict[client_ip], data['acceleration']['y'])

    filename = f'save_{client_ip}.npy'
    np.save(filename, client_data_dict[client_ip])

    return 'OK'


@app.route('/assign_role', methods=['GET'])
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


@app.route('/jump')
def jump():
    return render_template('jump.html')

@app.route('/redgreen')
def redgreen():
    return render_template('redgreen.html')

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
