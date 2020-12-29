import socket, threading, netHelper, socketserver, time


global fdic

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        sock = self.request[1]
        sock.sendto(fdic[data]())

       
 




class Networker: 
    def create_Networker(role, fdic=[]):
        if role =="S" and fdic:
            srvr = socketserver.UDPServer((netHelper.getIP(), 4230), UDPHandler)
            srvr.serve_forever()
        elif role == "C":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            HOST_IP = input("Enter Host IP: ")
            sock.sendto("connecting", (HOST_IP, 4230))

        else:
            print("you failed")

    def gimmedic(dic: dict):
        fdic = dic

    def create_Response():
        return g






isHost = True
print("Server Mode Selected. Starting now...")
listener = threading.Thread(target=hostServer, args=(1,), daemon=True)
listener.start()

