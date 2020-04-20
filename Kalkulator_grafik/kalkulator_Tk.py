from tkinter import *
import tkinter.messagebox
from tkinter import ttk

t = Tk(className = 'Kalkulator')
t.geometry('450x550')

operatori = ""  #promenljiva koja hvata unos sa dugmeta
hvata_unos = StringVar()  # upisuje oznaku na dugmetu u ekran za tekts Entery

# operatori = operatori +string(naznacen u broju ako je u buttonu 1 pise broj 1)
# hvata_unos setuje operatori tj. simbol koji je pritisnut i upisuje u skrin 
# oper
def pisanje(broj):  # parametar broj menjamo za oznaku dugmeta i ispisuje oznaku dugmeta
    global operatori
    operatori = operatori+str(broj) # promenljiva operatori je prazna
                                #ona je jednaka operatori i string broj 
                                # koji ispisuje oznaku dugmeta
    hvata_unos.set(operatori)# zamenjuje broj parametar sa brojem naznacen u lambda

def racunaj(hvata_unos):
    global operatori
    try:
        rezultat = eval(operatori) # eval se koristi kada treba da se procene neki matematicki
                                        # izrazi. Takodje procenjuje izraz niza i vraca celi br kao rezultat
        hvata_unos.set(rezultat)# eval funkcija vrednuje string iz izraza vraca ceo broj
        operatori = ""
    except:
        hvata_unos.set("error")
        tkinter.messagebox.showinfo("Error","Doslo je do greske.") 


def brisanje():
    global operatori
    operatori = "" 
    hvata_unos.set("")
    

skrin = Entry(t, font=("Courier New",12,'bold'), textvar=hvata_unos, width=25)
skrin.place(x = 105, y = 100)

b0 = Button(t, text="0", width=5, font = "bold", bg="black", fg="white", height=2, command = lambda:pisanje(0))
b0.place(x = 180, y = 400)

b1 = Button(t, text="1", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(1))
b1.place(x = 125, y = 350)

b2 = Button(t, text="2", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(2))
b2.place(x = 180, y = 350)

b3 = Button(t, text="3", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(3))
b3.place(x = 235, y = 350)

b4 = Button(t, text="4", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(4))
b4.place(x = 125, y = 300)

b5 = Button(t, text="5", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(5))
b5.place(x = 180, y = 300)

b6 = Button(t, text="6", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(6))
b6.place(x = 235, y = 300)

b7 = Button(t, text="7", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(7))
b7.place(x = 125, y = 250)

b8 = Button(t, text="8", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(8))
b8.place(x = 180, y = 250)

b9 = Button(t, text="9", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje(9))
b9.place(x = 235, y = 250)

b_procenat = Button(t, text="%", width=5, font = "bold", bg="black", fg="white", height=2, command = lambda:pisanje("%"))
b_procenat.place(x = 125, y = 400)


b_zarez = Button(t, text=",", width=5, font = "bold", bg="black", fg="white", height=2 , command = lambda:pisanje(","))
b_zarez.place(x = 235, y = 400)

b_jednako = Button(t, text="=", width=5, font = "bold", bg="black", fg="white", height=5, command = lambda:racunaj(hvata_unos))
b_jednako.place(x = 290, y = 348)

b_plus = Button(t, text="+", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje("+"))
b_plus.place(x = 290, y = 300)

b_minus = Button(t, text="-", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje("-"))
b_minus.place(x = 290, y = 250)

b_puta = Button(t, text="*", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje("*"))
b_puta.place(x = 125, y = 200)

b_podeljeno = Button(t, text="/", width=5, font = "bold",bg="black", fg="white", height=2, command = lambda:pisanje("/"))
b_podeljeno.place(x = 180, y = 200)

b_del = Button(t, text="C", width=11, font = "bold",bg="black", fg="white", height=2, command = lambda:brisanje())
b_del.place(x = 235, y = 200)

t.mainloop()