import socket
import sys
import exploits


print('______ _             _        _____ _                         ')
print('| ___ (_)           (_)      /  __ \ |                        ')
print('| |_/ /_  __ _  __ _ _  ___  | /  \/ |__   ___  ___  ___  ___ ')
print('| ___ \ |/ _` |/ _` | |/ _ \ | |   | _ \ / _ \/ _ \/ __|/ _ \ ')
print('| |_/ / | (_| | (_| | |  __/ | \__/\ | | |  __/  __/\__ \  __/')
print('\____/|_|\__, |\__, |_|\___|  \____/_| |_|\___|\___||___/\___|')
print('          __/ | __/ |                                         ')
print('         |___/ |___/                                          ')





        
def exploit():
    print('------ULTIMATE_PWNAGE------')
    print('Type list To List Exploits')
    print('Exploit syntax: <exploit name>')
    
    inp = (':>')
    
    
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
    print('------------CONTROL PANEL------------')
    print('     1.Listener                      ')
    print('     2.Generate A Payload            ')
    print('-------------------------------------')
    inp = input(':>')
    
    if inp == '1':
        
        print('Listening')
        while True:
            conn, addr = serv.accept()
            from_client = ''
            with conn:
                print('Connection Established')
                print('Session Created with' , addr)
                print('------YOU''RE IN----------')
                print('      1. Exploits         ')
                print('      2. Shell            ')
                print('      3. Exit             ')
                print('--------------------------')
                 

                
    elif inp == '2':
        print('WIP')
        '''
               WIP
            rhost = input('RHOST:>')
            rport = input('RPORT:>')
            payload = open('payload.txt', 'w')
            print('Generating payload /')
            payload.write
            time.sleep(0.5)
            os.system('cls')
            payload.write()
            
            '''
    elif inp == '3':
        exit()
            
main(input('Enter listening IP:>'))

