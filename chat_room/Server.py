import socket, sys, threading                                            
from _thread import *

class Server():
    def __init__(self, server_socket, server_host, server_ip, server_port):
        self.server_socket = server_socket
        self.server_host = server_host
        self.server_ip = server_ip
        self.server_port = server_port

    def binding(self):
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # kreiranje socket konstruktora
        self.server_host = socket.gethostname()     # uzimanje imena lokalne masine
        self.server_ip = socket.gethostbyname(self.server_host) # ip adresa 
        self.server_port = 8080     # port
        #self.br_konekcija = 0  # broj konekcija
        try:
            self.server_socket.bind((self.server_host, self.server_port))   # bindovanje i podizanje servera
            print("Bindovanje je izvrseno!")
            
        except socket.error as e:
            print(str(e))
            sys.exit()
        # ovo je region koji sadrzi definiciju za konektovanje vise klijenta kao i prosledjivanje poslatih poruka ! neophodno je dodatno poboljsavanje
        #region nadogradnja za multi client connection 
        # def multi_klijent(konekcija):
        #     self.konekcija = konekcija

        #     self.konekcija.send(str.encode("Dobro dosao na server!"))
        #     while True:
        #         self.data = self.konekcija.recv(2048)
        #         self.resp = "Poruka od servera >> " + self.data.decode()
        #         if not self.data:
        #             break
        #         self.konekcija.sendall(str.encode(self.resp))
        #     print("Konekcija klijenta je zavrsena: ", konekcija)
        #     self.konekcija.close()
        #endregion

        self.server_socket.listen(5)    # osluskivanje broja konekcija

        conn, addr = self.server_socket.accept()    # prihvatanje nove konekcije
        print("Primljena nova konekcija od: {0}:{1}".format(addr[0], addr[1]))  # ispisujemo ip i por nove konekcije
        while True:

            self.res = conn.recv(1024)  # primamo riquest i sa recv 1024 broj bayta duzina poruke i velicina bafera
            print("Poruka od kljenta >> ", self.res.decode())   # kada se poruka primi potrebno je da se dekoduje
            self.msg = input("Ja >> ")
            conn.send(str.encode(self.msg)) # prilikom slanja poruka se enkoduje

            # start_new_thread(multi_klijent,(conn,))       # funkcija uzima definiciju kao i parametar od server instance conn
            # self.br_konekcija += 1    
            #print("Broj konekcija: ", self.br_konekcija)
        self.server_socket.close()  # zatvaranje konekcije

s = Server("A","W","D","Q") 
s.binding()

