import socket, threading, netHelper

messages = []
def hostServer(name):
    print("Listener started.")
    global messages
    while(True):
            data, addr = sock.recvfrom(1024)
            print(str(addr )+ ": " + str(data))
            messages.append(data.decode())

def sendMessage(name, msg):
    sock.sendto(msg.encode(), (RCV_IP, 4230))
    for i in range(100):
        sock.sendto("ping".encode(), (RCV_IP, 4230))



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((netHelper.getIP(), 4230))
print("Chat Client Starting")
RCV_IP = input("Enter IP to connect to: ")
listener = threading.Thread(target=hostServer, args=(1,),daemon=True)
listener.start()
while True:
    MSG = input("MESSAGE: ")
    sender = threading.Thread(target=sendMessage,args=(1,MSG),daemon=True)
    sender.start()
