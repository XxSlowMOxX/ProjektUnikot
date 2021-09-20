import socket
import threading
import netHelper
import socketserver
import time

messages = []
HOST_IP = ""
MSG_T = 0.2
PING_MSG = "PING"
last_ping = 0


def hostServer(name):
    srvr = socketserver.UDPServer((netHelper.getIP(), 30814), UDPHandler)
    srvr.serve_forever()


def hooker(name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global messages
    while True:
        if(len(messages) != 0):
            sock.sendto(messages.pop(0).encode(), (HOST_IP, 30814))
        else:
            sock.sendto(PING_MSG.encode(), (HOST_IP, 30814))
        print(sock.recv(1024))
        time.sleep(MSG_T)


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):

        data = self.request[0]
        sock = self.request[1]
        global last_ping
        if(str(data, "utf-8").lower() == PING_MSG.lower()):
            # print("RCVD")
            if(len(messages) != 0):
                sock.sendto(messages.pop(0).encode(), self.client_address)
            else:
                sock.sendto(str("Ping-ack").encode(), self.client_address)
        else:
            if(len(messages) != 0):
                sock.sendto(messages.pop(0).encode(), self.client_address)
            else:
                sock.sendto(str("ack").encode(), self.client_address)
            print("Received: " + str(data, "utf-8") + " and responded")


MODE = input("Enter Mode of Operation (H=Host/C=Client):")
isHost = False
if(MODE == "H"):
    isHost = True
    print("Server Mode Selected. Starting now...")
    listener = threading.Thread(target=hostServer, args=(1,), daemon=True)
    listener.start()
else:
    HOST_IP = input("Enter Host IP: ")
    hook = threading.Thread(target=hooker, args=(2,), daemon=True)
    hook.start()
while True:
    messages.append(input("MSG: "))
