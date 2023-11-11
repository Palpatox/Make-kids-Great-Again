from flask import Flask, render_template, request, send_file
import numpy as np

app = Flask(__name__, template_folder='templates', static_folder='templates')

# Initialize a dictionary to store accelerometer data for each client
client_data_dict = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_result', methods=['GET'])
def get_result():
    # Implement logic to process data and generate a result
    # For example, you can read data from the saved file and perform some computation

    # Replace this with your actual result generation logic
    result_data = {'result': 'Your result here'}

    # Return the result as JSON
    return result_data



@app.route('/accelerometer', methods=['POST'])
def accelerometer():
    data = request.json
    client_ip = request.remote_addr
    print("Accelerometer data received:", data['accelerationIncludingGravity']['y'], client_ip)

    # Check if the client already has an array, if not, initialize one
    if client_ip not in client_data_dict:
        client_data_dict[client_ip] = np.array([])

    # Add the received data to the client's array
    client_data_dict[client_ip] = np.append(client_data_dict[client_ip], data['acceleration']['y'])

    filename = f'save_{client_ip}.npy'
    np.save(filename, client_data_dict[client_ip])

    return 'OK'

@app.route('/redgreen')
def redgreen():
    return render_template('redgreen.html')

@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

@app.route('/playpage')
def playpage():
    return render_template('playpage.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
