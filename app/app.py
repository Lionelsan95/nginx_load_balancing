from flask import Flask
import socket
import uuid

app = Flask(__name__)

@app.route('/')
def hello():
    # Get the hostname
    hostname = socket.gethostname()
    
    # Get the IP Address
    ip_address = socket.gethostbyname(hostname)

    # Get the MAC address
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 8)][::-1])

    return f"Hello World! IP Address: {ip_address}, MAC Address: {mac_address}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
