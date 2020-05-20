import mysql.connector  # mysql modul za konektovanje sa python skriptom
from mysql.connector import Error   # modul koji nam pokazuje greske koje se javljaju pri pisanju upit
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk,Image   # pomocu PIL modula mozemo da ubacimo sliku u Tkinter prozor
import os

__version__ = "0.1"     # ovo je oznaka za verziju programa

# stao sam kod sredjivanja slike pronadji velicinu 1150x800.
# pokusaj da sredis tekst da bude abstraktan sredi font i dugmice kao i unos da tekst
# povezi funkcije sa mysql

#region Connect to mysql
try:
    povezivanje = mysql.connector.connect(host='localhost',     # u try blok se nalazi komanda za konektovanje
                                         database='Registracija',
                                         user='root',
                                         password='zcbqe231rya')  
except Error as e:  # ako nije uspela konekcija prikazuje gresku
    print("Error greska pri konektovanju", e)
#endregion

klik = True

def log_in():       # definicija  novog tkinter prozora kako bi se setovala pozadinska slika mora prethodni prozor da se zatvori
    global klik
    
    if klik == True:
        tik.destroy()   # ovako se zatvara prozor
        klik = False

    nov = Tk(className = "Log in")
    nov.geometry("600x350+680+200")
    image = Image.open("C:src\\bg.jpg") #ovo je putanja do slike
    photo = ImageTk.PhotoImage(image)   
    label = Label(image = photo)    # ovde postavljamo sliku za pozadinu
    label.image = photo

    unos_mail = Entry(nov, width = 35)
    unos_mail.place(x = 210, y = 140)
    unos_mail_txt = Label(nov, text = "Enter email", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
    unos_mail_txt.place(x = 210, y = 115)

    unos_lozinka = Entry(nov, width = 35, show = "*")
    unos_lozinka.place(x = 210, y = 190)
    unos_lozinka_txt = Label(nov, text = "Enter password", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
    unos_lozinka_txt.place(x = 210, y = 165)

    reset = Button(nov, text = "Forgot password ?", bg = "#ffffff", fg="black", font = ("Helvetica", 8, "bold italic"), pady=3, padx=5 )
    reset.place(x = 430, y = 10)

    sign_in = Button(nov, text = "Sign in", bg = "#ffffff", fg="black", font = ("Helvetica", 8, "bold italic"), pady=3, padx=5 )
    sign_in.place(x = 280, y = 230)


    label.pack()



   
    nov.mainloop()

#region Tkinter window
tik = Tk(className = "Registration")
tik.geometry('1150x800+450+150')
#endregion
#region Tkinter image
image = Image.open("C:src\\bg.jpg") #ovo je putanja do slike
photo = ImageTk.PhotoImage(image)   
label = Label(image = photo)    # ovde postavljamo sliku za pozadinu
label.image = photo
label.pack(side = "top", fill = "both")
#endregion
#region Variables
CheckVar1 = IntVar()            # promenljive za hvatanje teksta koji je unesen
hvata_ime = StringVar()
hvata_prezime = StringVar()
hvata_password = StringVar()
re_password = StringVar()
hvata_email = StringVar()
#endregion
#region Fuction
def klik_prijava():     # funkcija dugmeta
    pass

def uzmi_info():
    info_korisnik = ime.get()               # funkcija get i set koje nam daju stringov koji su uneseni od strane korisnika
    info_prezime = prezime.get()
    info_email = email.get()
    info_password = lozinka.get()
    reinfo_password = ponavljanje_lozinke.get()

    if len(info_korisnik and info_prezime and info_password  and reinfo_password and info_email) == 0:          # ovo su uslovi koji moraju da se izvrse kako bi se uspesno registrovali i bili upisani u bazu 
        tkinter.messagebox.showinfo("Warning","It is not possible to create an account without value !")
    elif len(info_korisnik) <= 3:
        tkinter.messagebox.showinfo("Warning","Less than 3 characters per username are allowed !")
    elif len(info_prezime) <= 3:
        tkinter.messagebox.showinfo("Warning","No less than 3 last name characters allowed !")
    elif "@" not in info_email:
        tkinter.messagebox.showinfo("Warning","This is not an email address it is necessary to have an '@' tag.")
    elif len(info_password and reinfo_password) <= 3 : 
        tkinter.messagebox.showinfo("Warning","Your password is too short no less than 6 characters allowed \n \t\tand no spaces !")
    elif info_password == reinfo_password or reinfo_password == info_password:
        #region Write to mysql
        query  = povezivanje.cursor()   # ovo je prozor u kome se pise upit njega selektuje iz baze Registracija
        upit = "INSERT INTO korisnik (ime, prezime, adresa, lozinka) VALUES (%s,%s,%s,%s)"  # ovako se upisuje vrednost u kolone %s - oznacava kolone
        vrednost = (info_korisnik, info_prezime, info_email, info_password)   # ovo su vrednosti koje se upisuju
        query.execute(upit, vrednost)    # promenljive se stavljaju u execute
        povezivanje.commit()
        print(query.rowcount,"Uspesno unesen u Bazu podataka korisnik: {0}".format(info_korisnik))   # prikazuje uspesno izvrsavanje
        #endregion
        tkinter.messagebox.showinfo("Successfully","Account successfully created !")
    else:
        tkinter.messagebox.showinfo("Warning","Password entered incorrectly! \n \tTry again.")

    #region Deleting input
    hvata_ime.set("")       # nakon stiska dugmeta brise se unos
    hvata_prezime.set("")
    hvata_email.set("")
    hvata_password.set("")
    re_password.set("")
    #endregion

#endregion
#region Forms
ime = Entry(tik, width = 35, textvariable=hvata_ime)
ime.place(x = 500, y = 200)
ime_tekst = Label(tik, text = "First Name", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
ime_tekst.place(x = 500, y = 177)

prezime = Entry(tik, width = 35, textvariable=hvata_prezime)
prezime.place(x = 500, y = 250)
ime_tekst = Label(tik, text = "Last Name", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
ime_tekst.place(x = 500, y = 227)

lozinka = Entry(tik, width = 35, textvariable=hvata_password, show = "*")
lozinka.place(x = 500, y = 300)
ime_tekst = Label(tik, text = "Password", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
ime_tekst.place(x = 500, y = 277)

ponavljanje_lozinke = Entry(tik, width = 35, textvariable=re_password, show = "*")
ponavljanje_lozinke.place(x = 500, y = 350)
ime_tekst = Label(tik, text = "Conform Password", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
ime_tekst.place(x = 500, y = 327)

email = Entry(tik, width = 35, textvariable=hvata_email)
email.place(x = 500, y = 400)
ime_tekst = Label(tik, text = "Email", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
ime_tekst.place(x = 500, y = 377)

prijava = Button(tik, text = "Create accaunt", command = uzmi_info, bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"), pady=3, padx=5)
prijava.place(x = 675, y = 430)

log = Button(tik, text = "Login", command = log_in, bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"), pady=3, padx=5 )
log.place(x = 1050, y = 10)

cek_box = Checkbutton(tik, text = "Send news about service,\n offers and products to E-mail.", variable = CheckVar1 ,onvalue = 1, offvalue = 0, bg = "#ffffff", fg="black", font = ("Helvetica", 7, "bold italic"))
cek_box.place(x = 500, y = 430)

#endregion

tik.mainloop()
