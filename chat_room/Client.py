import socket, sys

class Klijent():
    def __init__(self, klijent_socket, klijent_host, klijent_ip, klijent_port):
        self.klijent_socket = klijent_socket
        self.klijent_host = klijent_host
        self.klijent_ip = klijent_ip
        self.klijent_port = klijent_port

    def konekcija(self):
        self.klijent_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.klijent_host = socket.gethostname()
        self.klijent_ip = socket.gethostbyname(self.klijent_host)
        self.klijent_port = 8080

        try:
            self.klijent_socket.connect((self.klijent_host, self.klijent_port))     # slanje requesta konekcije / mogao je da se i nadje input za unos 
            print("Konektovan si na server!")
        except socket.error as e:
            print(str(e))
            sys.exit()

        while True:
            
            self.msg = input("Ja >> ")
            self.klijent_socket.send(str.encode(self.msg))
            self.res = (self.klijent_socket.recv(1024))
            print("Poruka od servera >> ",self.res.decode())
        self.klijent_socket.close()
k = Klijent("S","G","H","X")
k.konekcija()












#https://www.askpython.com/python/examples/create-chatroom-in-python
#nauci malo vise 
