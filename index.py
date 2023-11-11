from flask import Flask, request, jsonify, send_file, Response, send_from_directory
from flask_cors import CORS
from OpenSSL import SSL

app = Flask(__name__, static_folder='public_html')


@app.route('/')
def hello():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    context = ('config/cert.pem', 'config/key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context)
    