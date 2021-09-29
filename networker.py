import socket
import threading
import netHelper
import socketserver
import time

messages = {}
connections = []

MSG_TIME = 0.2

def hooker(name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global messages
    while True:
        if (len(messages["192.168.178.78"]) != 0):
            sock.sendto("#".join(messages[connections[0]]).encode(), (connections[0], 30814))
            messages[connections[0]].clear()
            print("sent")
            print(sock.recv(4096).decode())
        else:
            sock.sendto("empty#".encode(), (connections[0], 30814))
            print(sock.recv(4096).decode())
        #for cmd in ret.split("#"):
         #   cmdHandler(cmd)
        time.sleep(MSG_TIME)


def hostServer(name):
    srvr = socketserver.UDPServer((netHelper.getIP(), 30814), UDPHandler)
    srvr.serve_forever()

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        data = self.request[0]
        sock = self.request[1]

        print(self.client_address[0] + " : " + str(data, "utf-8"))

        if self.client_address[0] not in messages:
            connections.append(self.client_address[0])
            messages[self.client_address[0]] = []

        for connection in connections:
            if (connection != self.client_address[0]):
                messages[connection].append(str(data, "utf-8"))

        print(messages)

        if(len(messages[self.client_address[0]]) != 0):
            sock.sendto("#".join(messages[self.client_address[0]]), self.client_address)
        sock.sendto(str("empty#").encode(), self.client_address)



def host():
    print("ServerMode:")
    listener = threading.Thread(target=hostServer, args=(1,), daemon=True)
    listener.start()

def client(HOST_IP):
    print("ClientMode")
    connections.append(HOST_IP)
    hook = threading.Thread(target=hooker, args=(2,),daemon=True)
    hook.start()

def cmdHandler(cmd):
    print(cmd)

m = input("Mode")
if (m == "h"):
    host()
    while True:
        a = 1
else:
    client("192.168.178.78")
    messages["192.168.178.78"] = []
    while True:
        messages["192.168.178.78"].append(input("M:"))