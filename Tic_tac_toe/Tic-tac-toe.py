
from tkinter import *   # ovo je modul pomocu kog smo kreirali prozor za igru i dugmice kao i info prozor
import tkinter.messagebox

# Ukoliko ne postoji kombinacija za pobedu neophodno je dodati tu kombinaciju program 


win = Tk(className = " X vs O")  # ovako se kreira Tkinter prozor 
win.geometry("750x550")     # Dimenzije prozora

click = True    # klik misom je tacan = True


'''Pravila igre: Pobednik je onaj koji nadoveze tri znaka
    u jednom redu bez prekida.'''

def provera(buttons):
    global click    # global je poznata funkcija mozemo ukljuciti nesto definisano u nasem kodu i pozivati ga pomocu globala
    if buttons["text"] == " " and click == True:    
        buttons["text"] = "X"
        click = False        # ako je dugme prazno i klik je jednak tacno onda 
                            #je dugme jednako X a klik je netacan = False ispisuje X

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"       
        click = True
    
    elif (b["text"] == "X" and b1["text"] == "X" and b2["text"] == "X" or
        b3["text"] == "X" and b4["text"] == "X" and b5["text"] == "X" or
        b6["text"] == "X" and b7["text"] == "X" and b8["text"] == "X" or
        b3["text"] == "X" and b4["text"] == "X" and b6["text"] == "X" or
        b["text"] == "X" and b4["text"] == "X" and b8["text"] == "X" or   
        b["text"] == "X" and b3["text"] == "X" and b6["text"] == "X" or    
        b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or    
        b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
        b2["text"] == "X" and b4["text"] == "X" and b6["text"] == "X"):
        tkinter.messagebox.showinfo("Igra je zavrsena", "Pobednik je X!")   # ovo je tkinfo prozor koji iskace ako neko pobedi
        #ovo su kombinacije kako moze da se pobedi ja sam krenuo sa brojanjem od 0 

    elif (b["text"] == "O" and b1["text"] == "O" and b2["text"] == "O" or
        b3["text"] == "O" and b4["text"] == "O" and b5["text"] == "O" or
        b6["text"] == "O" and b7["text"] == "O" and b8["text"] == "O" or
        b3["text"] == "O" and b4["text"] == "O" and b6["text"] == "O" or
        b["text"] == "O" and b4["text"] == "O" and b8["text"] == "O" or   
        b["text"] == "O" and b3["text"] == "O" and b6["text"] == "O" or    
        b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or    
        b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
        b2["text"] == "O" and b4["text"] == "O" and b6["text"] == "O"):
        tkinter.messagebox.showinfo("Igra je zavrsena", "Pobednik je O!")
    else:
        tkinter.messagebox.showinfo("Igra je zavrsena", "Nema pobednika pokusaj ponovo!")
        # ako nema pobednika ovo iskace kao obavestenje da nema pobednika
buttons = StringVar()

b = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b)) # ovako se kreira dugme sadrzi text koji je prazan font kao i visinu
                                                                                                    # i sirinu dugmeta i command koji smo povezali sa def provera lambda jos nisam stigo
                                                                                                    # do tog dela u knjizi
b.pack()
b.place(x = 105, y = 30)   # ovo je lokacija gde se nalazi dugme u prozoru 

b1 = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b1))
b1.pack()
b1.place(x = 265, y = 30)

b2 = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b2))
b2.pack()
b2.place(x = 425, y = 30)
    
b3 = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b3))
b3.pack()
b3.place(x = 105, y = 195)

b4 = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b4))
b4.pack()
b4.place(x = 265, y = 195)

b5 = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b5))
b5.pack()
b5.place(x = 425, y = 195)

b6 = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b6))
b6.pack()
b6.place(x = 105, y = 360)

b7 = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b7))
b7.pack()
b7.place(x = 265, y = 360)

b8 = Button(win, text=" ", font = ('Times 10 bold'), width=20, height=10, command=lambda:provera(b8))   
b8.pack()
b8.place(x = 425, y = 360)
    
    

win.mainloop()  # ovako se zatvara kraj programa 
