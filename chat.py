import socket, threading, netHelper, socketserver, time




messages = []
HOST_IP = "141.70.1.76"
MSG_T = 0.1

def hostServer(name):
    srvr = socketserver.UDPServer((netHelper.getIP(), 4230), UDPHandler)
    srvr.serve_forever()

def hooker(name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global messages
    i = 0

    sock.sendto(str(i).encode(), (HOST_IP, 4230))
    while True:
        print(sock.recv(1024))




class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        sock = self.request[1]



#MODE = input("Enter Mode of Operation (H=Host/C=Client):").lower()
MODE = "C"
isHost = False
if(MODE == "h"):
    isHost = True
    print("Server Mode Selected. Starting now...")
    listener = threading.Thread(target=hostServer, args=(1,), daemon=True)
    listener.start()
else:
    if not HOST_IP:
        HOST_IP = input("Enter Host IP: ")

    hook = threading.Thread(target=hooker, args=(2,), daemon=True)
    hook.start()


while True:
    time.sleep(5)
