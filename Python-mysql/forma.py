import mysql.connector  # mysql modul za konektovanje sa python skriptom
from mysql.connector import Error   # modul koji nam pokazuje greske koje se javljaju pri pisanju upita
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

mail_sifra = os.getenv('mailsifra')
dbpass = os.getenv('dbpassword')
#region Connect to mysql
try:
    povezivanje = mysql.connector.connect(host='localhost',     # u try blok se nalazi komanda za konektovanje
                                         database='Registracija',
                                         user='root',
                                         password='{0}'.format(dbpass))
except Error as e:  # ako nije uspela konekcija prikazuje gresku
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
    image = Image.open("C:src\\bg.jpg") 
    photo = ImageTk.PhotoImage(image)   
    label = Label(image = photo)    
    label.image = photo
    label.pack()
    
    #region progres bar
    # PROGRES BAR : nadji nacin kako da ga startujes kada se otvori prozor 
    #Problem je u tome sto se prozor koci i bar se startuje pre otvaranja prozora zbog sleepa traje 5-6 sec kada dodje do 100% tek tada se otvara prozor
    # s = Style(sec)
    # s.layout("LabeledProgressbar",
    #     [('LabeledProgressbar.trough',
    #     {'children': [('LabeledProgressbar.pbar',
    #                     {'side': 'left', 'sticky': 'ns'}),
    #                     ("LabeledProgressbar.label",
    #                     {"sticky": ""})],
    #         'sticky': 'nswe'})])
    # p = Progressbar(sec, orient= HORIZONTAL, length=200, mode="determinate",style="LabeledProgressbar" )
    # p.place(x = 350, y = 100)
    # s.configure("LabeledProgressbar", text="0 %      ")
    # def bar():
        
    #     if a == 1: 
    #         for i in range (101):
    #             time.sleep(0.05)
    #             p["value"] = i
    #             s.configure("LabeledProgressbar", text="{0} %      ".format(i))
    #             sec.update_idletasks()
                
    #         p["value"] = 0
    #     else:
    #         tkinter.messagebox.showinfo("Warning","Some dataType is gone wrong!")
    #endregion  
    # ovo cu naknadno da dodam prvo moram da smislim nacin gde da ga smestim i kako da ga aktiviram a da se ne desava greska 
  
    sec.mainloop()
    
def log_in():       # definicija  novog tkinter prozora kako bi se setovala pozadinska slika mora prethodni prozor da se zatvori
    global klik
    
    if klik == True:
        tik.destroy()   # ovako se zatvara prozor
        klik = False

    nov = Tk(className = "Log in")
    nov.geometry("600x350+680+200")
    nov.resizable(False,False)
    image = Image.open("C:src\\bg.jpg") #ovo je putanja do slike
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
                image = Image.open("C:src\\bg.jpg") #ovo je putanja do slike
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
                                             
                    Your new password is {1} , after logging in again press options> account> password.'''.format(r_mail, lista[0]))

                    cor = 1

                    for row in korisnik:

                        try:
                            
                            mycursor = povezivanje.cursor()

                            sql = "UPDATE korisnik SET lozinka = '{0}' WHERE korisnik_id = '{1}'".format(lista[0], row[0])
      
                            mycursor.execute(sql)
                            povezivanje.commit()

                            if cor == 1:
                                pass
                                tkinter.messagebox.showinfo("Verification","Ваша нова лозинка је спремна и послата на е  адресу.")
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

    def sign_prov ():
        
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
        
            # 1. sredi izbacivanje greske za pogresan mail i pass
            # 2. dodaj nesto tipa s = succesefully return s za oepn novog prozora nakon logovanja ako je mail i pass postojecci
            # 3. napravi prozor za reset passa
            # 4. u generator pasa dodaj i brojeve
            # 5. spoji sa forgot password
            # 6. napravi svoj kod za slanje maila kako bi naucio kako to radi
            # 7. nadji kako da napravis neki conform za email tipa xml..
            # 8. ako su 3,4,5,6,7 napravi da je lozinka za reset duzine trajanja 5-10 min 
            # 9. nakon reset pasa treba nam nova lozinka za korisnika 
            # koraci 
            
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
    global mail_sifra
    info_korisnik = ime.get()               # funkcija get i set koje nam daju stringove koji su uneseni od strane korisnika
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
