import socket, threading, netHelper, socketserver, time

messages = []
HOST_IP = ""
MSG_T = 0.2
PING_MSG = "PING"
last_ping = 0
wait_time = 25

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
            sock.sendto(PING_MSG.encode(), (HOST_IP, 4230))
        time.sleep(MSG_T)

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        
        global wait_time
        data = self.request[0]
        sock = self.request[1]
        time.sleep(wait_time)
        global last_ping
        if(str(data, "utf-8").lower() == PING_MSG.lower()):
            print("RCVD")
        else:            
            sock.sendto(str(last_ping).encode(), self.client_address)
            print("Received: " + str(data, "utf-8") + "  with wait time: " + str(wait_time) + " and responded")
            if(int(str(data, "utf-8")) != last_ping+1):
                print("Packet Lost between: " + str(last_ping)  + " and " + str(data, "utf-8"))
            last_ping = int(str(data, "utf-8"))
            wait_time += 5

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