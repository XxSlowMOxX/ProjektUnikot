import socket, threading, netHelper, socketserver, time

messages = []
HOST_IP = ""
MSG_T = 0.2

def hostServer(name):
    srvr = socketserver.UDPServer((netHelper.getIP(), 4230), UDPHandler)
    srvr.serve_forever()

def hooker(name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global messages
    while True:
        if(len(messages) != 0):
            sock.sendto(messages.pop(0).encode(), (HOST_IP, 4230))
        else:
            sock.sendto("PING".encode(), (HOST_IP, 4230))
        time.sleep(MSG_T)


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        sock = self.request[1]
        print(self.client_address[0] + " : " + data)



MODE = input("Enter Mode of Operation (H=Host/C=Client):")
isHost = False
if(MODE == "H"):
    isHost = True
    print("Server Mode Selected. Starting now...")
    listener = threading.Thread(target=hostServer, args=(1,), daemon=True)
    listener.start()
else:
    HOST_IP = input("Enter Host IP: ")
    hook = threading.Thread(target=hooker, args=(1,), daemon=True)
    hook.start()
while True:
    messages.append(input("MSG: "))