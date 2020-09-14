import mysql.connector  # mysql modul za konektovanje sa python skriptom
#from mysql.connector import error  # modul koji nam pokazuje greske koje se javljaju pri pisanju upita
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk,Image   # pomocu PIL modula mozemo da ubacimo sliku u Tkinter prozor
from tkinter.ttk import Progressbar, Style      # modul za popunjujucu liniju
import time
from win10toast import ToastNotifier # modul za notifikaciju destopa
import smtplib, getpass # modul smtp port
from email.mime.multipart  import MIMEMultipart
from email.mime.text  import MIMEText
import random   # modul za nasumican izbor
import string   # asci lista karaktera mali i velikih 
import os

__version__ = "0.1"     # ovo je oznaka za verziju programa

mail_sifra = os.getenv('mailsifra') # env variablaa za password iz sistema
dbpass = os.getenv('dbpassword')
#region Connect to mysql
try:
    povezivanje = mysql.connector.connect(host='localhost',     # u try blok se nalazi komanda za konektovanje
                                         database='registracija',
                                         user='root',
                                         password='{0}'.format(dbpass))
except povezivanje.error as e:  # ako nije uspela konekcija prikazuje gresku
    print("Error greska pri konektovanju", e)
    exit()

#endregion

klik = True
mail_suc = 0
cor = 0
a = 1

def dobro_dosao():
    global klik

  

    sec = Tk(className = "Welcome")
    sec.geometry("920x800+500+100")
    sec.resizable(False,False)
    image = Image.open("C:\\Users\\Milos\\Desktop\\bg.jpg") 
    photo = ImageTk.PhotoImage(image)   
    label = Label(image = photo)    
    label.image = photo
    label.pack()
    
    jednokratni_passw = StringVar()
    new_pass = StringVar()
    rep_pass = StringVar()
    def change_pass(): 
        check_jednokratni_pass = 0

        # ako nije jasno sta je provera_1.. iza znaka jednaksti je varibla sa vrednostima stringvar koja hvata unesen text iz entery polja 
        # sa nesto.get() vracamo tekst iz polja za unos u variablu provera_1 i pritom prikazujemo to radimo da mozemo da upisemo stvari u bazu podataka
        provera_1 = jednokratni_passw.get()
        provera_2 =  new_pass.get()
        provera_3 = rep_pass.get()

        # komanda za kreiranje prozora za restartovanje passworda
        jednokratni_pass = Entry(sec, width = 35, show = "*", textvariable = jednokratni_passw)
        jednokratni_pass.place(x = 400, y = 300)
        txt_jednokratni_pass = Label(sec, text = "Enter one-time password", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
        txt_jednokratni_pass.place(x = 400, y = 275)

        unos_pass_new = Entry(sec, width = 35, show = "*", textvariable = new_pass)
        unos_pass_new.place(x = 400, y = 360)
        txt_pass_new = Label(sec, text = "Enter new password", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
        txt_pass_new.place(x = 400, y = 335)

        unos_pass_rep = Entry(sec, width = 35, show = "*", textvariable = rep_pass)
        unos_pass_rep.place(x = 400, y = 420)
        txt_pass_rep = Label(sec, text = "Repeat password", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
        txt_pass_rep.place(x = 400, y = 395)

        old_pass = Button(sec, text = "Change password", command = change_pass,  bg = "#ffffff", fg="black", font = ("Helvetica", 8, "bold italic"), pady=3, padx=5 )
        old_pass.place(x = 400, y = 450)


        try:
            query  = povezivanje.cursor()
            sql_select = "select lozinka from registracija.korisnik WHERE lozinka = '{0}'".format(provera_1)      # provera za password da li se nalazi u nasoj bazi
            query.execute(sql_select)   # izvrsava upit
            rekord = query.fetchall()   # vraca sve redove iz upita
            re_password = ''.join(rekord[0]) # rekord vraca tuplu sa joinom dobijamo informaciju iz baze

            print(re_password)
            check_jednokratni_pass = 1 # variabla koja nam pokazuje da je jednokratni password postojeci u bazi podataka
        except:
            print("one-time password incorect!")

        if check_jednokratni_pass == 1: # ako je jedan znaci da je try blok izvrsen
            
            if len(provera_2 and provera_3) <= 5 : 
                tkinter.messagebox.showinfo("Warning","Your password is too short no less than 6 characters allowed \n \t\tand no spaces !")

            elif provera_2 == provera_3 or provera_3 == provera_2:    # dve lozinke moraju da budu iste inace nece uci u sledeci blok
                print(provera_2, " / ", provera_3)

                
                try:
                    query  = povezivanje.cursor()
                    sql_select = "UPDATE korisnik SET lozinka = '{0}' WHERE ime = 'laza'".format(provera_2)
                    query.execute(sql_select)  
                    rekord = query.fetchall()                                           
                    new_password = ''.join(rekord[0]) 
                    print(new_password)
                    tkinter.messagebox.showinfo("Successfully","You have successfully changed the password !")
                except:
                    print("Error")
                

                   # zbog  rekord = query.fetchall()  se ne izvrsava sledeci deo koda pokusaj da izmenis imena mozda se mesa sa prethodnim upitom jel su u istoj definiciji:
                   # pokusaj onda da stavis poseban def blok i pozovi ga da vidids da li oce tako ako nje googlaj i vidi sta kazu formi 
                   # cilj je upisati novu lozinku u DB za to imas generisan password ali sta ako neko oces da pormeni lozinku i bez povracaja a postoje dve iste npr"1234" razmisli o idu ili emailu kao i sql upitima!
    
        else:
            pass
     
        
        # nakon pritisnutog dugmeta setujemo tekst "" - kako bi dobili prazno polje
        jednokratni_passw.set("")
        new_pass.set("")
        rep_pass.set("")

    def return_home():
        # komanda za unistavanje prozora koja pritom otvara novi pocetni prozor
        # dobijamo efekat vracanja pocetne stranice
        sec.destroy()

        dobro_dosao()
        
    menu_bar = Menu(sec)    # menu bar sa opcijama 
    # ovde smo kreirali sadrzaj menua i dodelili komande kako i sta ce da se izvrrava
    file_menu = Menu(menu_bar, tearoff = 0)
    file_menu.add_command(label = "Change password", command = change_pass)
    file_menu.add_command(label = "Change username", command = change_pass)
    file_menu.add_separator()
    file_menu.add_command(label = "Return to home ", command = return_home)
    menu_bar.add_cascade(label = "Settings", menu = file_menu)

    sec.config(menu = menu_bar)

    sec.mainloop()
    
def log_in():       # definicija  novog tkinter prozora kako bi se setovala pozadinska slika mora prethodni prozor da se zatvori
    global klik
    
    if klik == True:
        tik.destroy()   # ovako se zatvara prozor
        klik = False

    nov = Tk(className = "Log in")
    nov.geometry("600x350+680+200")
    nov.resizable(False,False)
    image = Image.open("C:\\Users\\Milos\\Desktop\\bg.jpg") #ovo je putanja do slike
    photo = ImageTk.PhotoImage(image)   
    label = Label(image = photo)    # ovde postavljamo sliku za pozadinu
    label.image = photo
    label.pack()

    mail_prov = StringVar()
    pass_prov = StringVar()
    def reset_password():
        global klik
        if a == 1:
            nov.destroy()
            if a == 1:
                               
                res = Tk(className="Forgot password ?")
                res.geometry("600x350+680+200")
                res.resizable(False,False)
                image = Image.open("C:\\Users\\Milos\\Desktop\\bg.jpg") #ovo je putanja do slike
                photo = ImageTk.PhotoImage(image)   
                label = Label(image = photo)    # ovde postavljamo sliku za pozadinu
                label.image = photo
                label.pack()

                res_mail = StringVar()
                
                def cmd_res():
                
                    r_mail = unos_mail_res.get()
                    
                    query  = povezivanje.cursor()
                    sql_pass = "select korisnik_id,adresa from registracija.korisnik WHERE adresa = '{0}'".format(r_mail)
                    query.execute(sql_pass) 
                    korisnik = query.fetchall()   
    
                    lista = []
                    randum_str = string.ascii_letters
                    bira_karakter = (random.choice(randum_str + string.digits)for i in range(9))
                    sifra = ''.join(bira_karakter)
                    lista.insert(0, sifra)


                    def mejl(tekst):    # pomocni parametar
                        global mail_sifra
                        password = mail_sifra
                        od = "mifa43kotez@gmail.com"    # od posiljalca
                        za = "{0}".format(r_mail)    # za primaoca
                        msg = MIMEMultipart()
                        msg["od"] = od
                        msg["za"] = za 
                        msg["Subject"] = "Python mail"

                        body = tekst
                        msg.attach(MIMEText(body, "Plain"))

                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.ehlo()
                        server.starttls()
                        server.login("mifa43kotez@gmail.com", password)
                        text = msg.as_string()
                        server.sendmail(od, za, text)
                        print("poslato")
                        return
                    mejl('''Dear users {0},
                                             
                    Your new password is {1} , after logging in again press Settings> Change password.'''.format(r_mail, lista[0]))

                    cor = 1

                    for row in korisnik:

                        try:
                            
                            mycursor = povezivanje.cursor()

                            sql = "UPDATE korisnik SET lozinka = '{0}' WHERE korisnik_id = '{1}'".format(lista[0], row[0])
      
                            mycursor.execute(sql)
                            povezivanje.commit()

                            if cor == 1:
                                pass
                                tkinter.messagebox.showinfo("Verification","Your new password is ready and sent to your email address.")
                        except:
                            print('Error in Sql.query')
    
                    res_mail.set("")

                unos_mail_res = Entry(res, width = 35, textvariable = res_mail)
                unos_mail_res.place(x = 210, y = 140)
                txt_mail_res = Label(res, text = "Enter email", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
                txt_mail_res.place(x = 210, y = 115)

                reset_it = Button(res, text = "Restart my password",command = cmd_res, bg = "#ffffff", fg="black", font = ("Helvetica", 8, "bold italic"), pady=3, padx=5 )
                reset_it.place(x = 250, y = 190)
 
                res.mainloop()

    def sign_prov():
       
        prov_mail = unos_mail.get()
        prov_pass = unos_lozinka.get()

        def sign_prov_mail():
            global cor
            global mail_suc

            try:
                query  = povezivanje.cursor()
                sql_select = "select adresa from registracija.korisnik WHERE adresa = '{0}'".format(prov_mail)      # provera za email da li se nalazi u nasoj bazi
                query.execute(sql_select)   # izvrsava upit
                rekord = query.fetchall()   # vraca sve redove iz upita
                mail = ''.join(rekord[0]) # rekord vraca mail kao tuplu sa joinok dobijamo mail iz baze

                if prov_mail == mail:
                    print("mail = {0}".format(mail))
                    mail_suc = 1        # ako je postojeci vrednost je 1
                 
                else:
                    pass
            except:
                print("Mail is wrong")
                tkinter.messagebox.showinfo("Warning","Incorect mail !")
                mail_suc = 0
            return mail_suc
        
            
        def sign_prov_pass():
            global klik
            global cor
            try:
                query  = povezivanje.cursor()
                sql_pass = "select lozinka from registracija.korisnik WHERE lozinka = '{0}' AND adresa = '{1}'".format(prov_pass, prov_mail)      # provera za lozinku da li se nalazi u nasoj bazi
                query.execute(sql_pass) 
                password = query.fetchall()   # vraca sve redove iz baze..      ^--- ovim se suzava krug pretrage tako sto uneseni mail ili  pass
                                                                                        #proverava da li postoji u bazi 
                password = ''.join(password[0])
                if prov_pass == password and mail_suc == 1: # samo ako je sifa istako kao u bazi i ako je mail = 1 onda je uspesno
                    print("password = ", password)
                    tkinter.messagebox.showinfo("Successfully","Successfully sign in !")
                    cor = 1 # ako su podaci tacni onda je cor = 1 i ulazi u blok zatvaranja programa
                   # ako su podaci ne postojeci nece uci u petlju terminal prikazuje gresku o nepoznatoj variabli ako je uso u petlju radi bez greske https://stackoverflow.com/questions/15921203/how-to-create-a-system-tray-popup-message-with-python-windows
                   
                else:
                    pass
            except:
                print("Password is wrong")
                tkinter.messagebox.showinfo("Warning","Incorect password !")


            def notif():
                try:
                    notifikacija = ToastNotifier()
                    notifikacija.show_toast("New mesage from GuiApp !",         # naslov notifikacije
                        "A new upgrade is an available click for more information.",  # poruka 
                        duration=7) # duzina trajanja
                except:
                    print("Something is wrong")
            
            if cor == 1:        # uslov za unistenje prozora
                nov.destroy()
                if cor == 1:        # otvaranje novog prozora
                    dobro_dosao()
                    pass
                    notif()     # nakon napustanja programa dobija se informacija o novom apgrejdu
            else:
                print("Something is wrong")

        sign_prov_mail()
        sign_prov_pass()

        mail_prov.set("")
        pass_prov.set("")
   
    #region forms for sign in
    unos_mail = Entry(nov, width = 35, textvariable = mail_prov)
    unos_mail.place(x = 210, y = 140)
    unos_mail_txt = Label(nov, text = "Enter email", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
    unos_mail_txt.place(x = 210, y = 115)

    unos_lozinka = Entry(nov, width = 35, show = "*", textvariable = pass_prov)
    unos_lozinka.place(x = 210, y = 190)
    unos_lozinka_txt = Label(nov, text = "Enter password", bg = "#ffffff", fg="black", font = ("Helvetica", 10, "bold italic"))
    unos_lozinka_txt.place(x = 210, y = 165)

    reset = Button(nov, text = "Forgot password ?", command =  reset_password, bg = "#ffffff", fg="black", font = ("Helvetica", 8, "bold italic"), pady=3, padx=5 )
    reset.place(x = 430, y = 10)

    sign_in = Button(nov, text = "Sign in", command = sign_prov, bg = "#ffffff", fg="black", font = ("Helvetica", 8, "bold italic"), pady=3, padx=5 )
    sign_in.place(x = 280, y = 230)
    #endregion
   
    nov.mainloop()

#region Tkinter window
tik = Tk(className = "Registration")
tik.geometry('1150x800+450+150')
tik.resizable(False,False)
#endregion
#region Tkinter image
image = Image.open("C:\\Users\\Milos\\Desktop\\bg.jpg") #ovo je putanja do slike
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
    global mail_sifra
    info_korisnik = ime.get()               # funkcija get i set koje nam daju stringove koji su uneseni od strane korisnika
    info_prezime = prezime.get()
    info_email = email.get()
    info_password = lozinka.get()
    reinfo_password = ponavljanje_lozinke.get()

    rand_num = "0123456789" # string sa brojnim vrednostima
    generisan_id = (random.choice(rand_num)for i in range(5)) # biramo nasumicno brojeve i uz for petlju odredjujemo duzinu 
    generisan_id = "".join(generisan_id) # spajamo vrednosti
    generisan_id = "#" + generisan_id # i dodajemo "#" ispred

    if len(info_korisnik and info_prezime and info_password  and reinfo_password and info_email) == 0:          # ovo su uslovi koji moraju da se izvrse kako bi se uspesno registrovali i bili upisani u bazu 
        tkinter.messagebox.showinfo("Warning","It is not possible to create an account without value !")
    elif len(info_korisnik) <= 3:
        tkinter.messagebox.showinfo("Warning","Less than 3 characters per username are allowed !")
    elif len(info_prezime) <= 3:
        tkinter.messagebox.showinfo("Warning","No less than 3 last name characters allowed !")
    elif "@" not in info_email:
        tkinter.messagebox.showinfo("Warning","This is not an email address it is necessary to have an '@' tag.")
    elif len(info_password and reinfo_password) <= 5 : 
        tkinter.messagebox.showinfo("Warning","Your password is too short no less than 6 characters allowed \n \t\tand no spaces !")
    elif info_password == reinfo_password or reinfo_password == info_password:
        #region Write to mysql
        query  = povezivanje.cursor()   # ovo je prozor u kome se pise upit njega selektuje iz baze Registracija
        upit = "INSERT INTO korisnik (ime, prezime, adresa, lozinka, id_app) VALUES (%s,%s,%s,%s,%s)"  # ovako se upisuje vrednost u kolone %s - oznacava kolone
        vrednost = (info_korisnik, info_prezime, info_email, info_password, generisan_id)   # ovo su vrednosti koje se upisuju
        query.execute(upit, vrednost)    # promenljive se stavljaju u execute
        povezivanje.commit()
        print(query.rowcount,"Uspesno unesen u Bazu podataka korisnik: {0}".format(info_korisnik))   # prikazuje uspesno izvrsavanje
        #endregion
        tkinter.messagebox.showinfo("Successfully","Account successfully created !")

        password = mail_sifra# polje za unos lozinke 

        def mejl(tekst):    # pomocni parametar
            od = "mifa43kotez@gmail.com"    # od posiljalca
            za = "{0}".format(info_email)    # za primaoca
            msg = MIMEMultipart()
            msg["od"] = od
            msg["za"] = za 
            msg["Subject"] = "Python mail"

            body = tekst
            msg.attach(MIMEText(body, "Plain"))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("mifa43kotez@gmail.com", password)
            text = msg.as_string()
            server.sendmail(od, za, text)
            print("poslato")
            return
        mejl('''Welcome {0},

        In our community Gui Application service comfortably accommodate and read more about us at: www.//guiapps.com.

        Thank you for your trust:
           GuiApps.'''.format(info_korisnik))

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
