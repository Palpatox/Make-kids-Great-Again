from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__, template_folder='templates')

# Initialize an empty array to store accelerometer data
accelerometer_data_array = np.array([])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accelerometer', methods=['POST'])
def accelerometer():
    data = request.json
    print("Accelerometer data received:", data['acceleration']['y'])
    global accelerometer_data_array

    # Add the received data to the array
    accelerometer_data_array=np.append(accelerometer_data_array,data['acceleration']['y'])
    np.save('save.npy',accelerometer_data_array)

    return 'OK'

if __name__ == '__main__':
    app.run(host='10.0.14.51', port=5000, debug=True)
