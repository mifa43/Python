import sounddevice as sd
from scipy.io.wavfile import write
import winsound
import speech_recognition as sr
import soundfile as sf
import webbrowser
import subprocess

lista = []
unos = int(input("Unesi broj '1' za unos glasovne poruke:"))

def rekorduj():
    global lista
    fs = 44100  # frekvencija u hz
    seconds = 5  # trajanje zvuka
    mojrekording = sd.rec(int(seconds * fs), samplerate=fs, channels=2) # kanali za snimanje
    sd.wait()  # pauziranje kako bi se snimijo zvuk
    write('output.wav', fs, mojrekording)  # pisanje i cuvanje zvuka u wav format

    winsound.Beep(1000, 100)    # beep winsound modul za slusanje snimljenog zvuka
    filename = "output.wav" # ekstenzija fajla je wav 
    winsound.PlaySound(filename, winsound.SND_FILENAME) #  plejer 

    data, samplerate = sf.read('output.wav')    # modul za konvertovanje wav fajla u \
    sf.write('output.flac', data, samplerate)  # flac fajl 
    # nisam bas strucan za audio produkciju ali koliko sam procitao razlika izmedju wav i flaca je u frekvenciji i kanala emitovanja
    # i iz tog razloga speech_recognition modul za pisanje zvucnih fajlova u txt fajlove ne moze da koristi wav, mp3.. itd audio formate ali mu odgovara flac

    r = sr.Recognizer() 
    hard = sr.AudioFile('output.flac') # audio fajl koji citamo 
    with hard as source:    # otvaranje i konvertovanje audio fajla u tekst 
        audio = r.record(source)
    rec_1 = r.recognize_google(audio)

    lista.insert(0, rec_1)  # u listu se dodaje izgovorena rec
    print(lista[0])
    for i in lista:     # sa for petljom proveravamo reci koje su unesene
        lista_cmds = ['open', 'do']     # lista cmd je lista kljucnih reci koje mozemo da pretvorimo u komande za izvrsavanje 
        for n in lista_cmds:    # proveravamo dali u listi izgovorene reci postoji i rec koja opisuje neku od reci iz liste komande
            if 'open' in i and 'open' in n:     # uslov ako je izgovorena rec open i ta rec ima u listi komanda izvrsavamo otvaranje necega >!< za sada je to otvaranje googla 
               
               
                subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                webbrowser.open("https://www.youtube.com")
                print("+1")

            
            

   





if unos == 1:
    rekorduj()