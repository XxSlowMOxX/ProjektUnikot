import socket, threading, netHelper

messages = []

def hostServer(name):
    print("Listener started.")
    global messages
    while(True):
            data, addr = sock.recvfrom(1024)
            if(str(data) == 'ping'):
                print("ping received")
            else:
                print(str(data))
            if(len(messages) != 0):
                sock.sendto(messages[0].encode(), addr)
                messages.pop()

def sendMessage(msg):
    messages.append(msg)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((netHelper.getIP(), 4230))
print("Chat Client Starting")
RCV_IP = input("Enter IP to connect to: ")
listener = threading.Thread(target=hostServer, args=(1,),daemon=True)
listener.start()
while True:
    MSG = input("MESSAGE: ")
    sendMessage(MSG)