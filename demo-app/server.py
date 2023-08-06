from flask import Flask, render_template_string
import socket
import time
import threading
import multiprocessing

app = Flask(__name__)

@app.route('/')
def home():
    host_name = socket.gethostname() 
    try:
        host_ip = socket.gethostbyname(host_name)
    except socket.gaierror:
        host_ip = 'Could not resolve IP'
    return render_template_string('<h1>Welcome to DevOps demo!</h1><p>Hostname: {{ hostname }}</p><p>IP: {{ ip }}</p>',
                                  hostname=host_name, ip=host_ip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
