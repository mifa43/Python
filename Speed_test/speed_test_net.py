
import speedtest    # modul za merenje specifikacija internet veze

lista = []  # lista koja belezi ping servera
speed = speedtest.Speedtest() 

class Testbrzine:   # kreiranje klase i njenih objekta

    global lista    # ukljucili smo atribute na globalnom nivou tako da vazi u nasoj klasi i objektima
    global speed

    def __init__(self, brzina_download, brzina_upload, brzina_ping):    # privatna instanca klase sa promenljivama  self je kljucna rec + promenljiva npr(brzina_download..)
        self.download = brzina_download     # ovako se sa kljucnom reci self dodeljuje promenljiva
        self.brzina_upload = brzina_upload
        self.brzina_ping = brzina_ping

    def brzina_interneta(self):  
        global lista
        global speed

        self.brzina_download = speed.download() # promenljiva dobija svoju funkciju za brzinu skidanja
        self.brzina_upload = speed.upload() # promenljiva dobija svoju funkciju za brzinu uploada
        self.brzina_ping = speed.get_servers(lista) # promenljiva dobija svoju funkciju za merenje pinga od servera i upisuje u listu
        self.brzina_ping = speed.results.ping   # rezultat iz liste

        print("Download : {0}\nUpload : {1}\nPing : {2}".format(self.brzina_download, self.brzina_upload, self.brzina_ping))    # ispisujemo na ekranu vrednosti koje smo dobili

t = Testbrzine('brzina_download', 'brzina_upload', 'brzina_ping')   # sa t smo skratili nas kod kako bi smo ga lakse pozvali. u Testbrzine ima 3 argumenta(brzina_download, brzina_upload, brzina_ping) i obavezno je da ih definisemo pri pozivanju klase
t.brzina_interneta() # ovako smo spojili privatnu klasu sa metodom 

