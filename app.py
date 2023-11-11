from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accelerometer', methods=['POST'])
def accelerometer():
    data = request.json
    print("Accelerometer data received:", data)
    return 'OK'

if __name__ == '__main__':
    app.run(host='10.0.14.51', port=5000, debug=True)
