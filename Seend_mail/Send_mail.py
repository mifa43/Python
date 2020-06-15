import smtplib, getpass # modul smtp port

from email.mime.multipart  import MIMEMultipart
from email.mime.text  import MIMEText

password = getpass.getpass("Unesi lozinku E-maila: ") # polje za unos lozinke 

def mejl(tekst):    # pomocni parametar
    od = "mifa43kotez@gmail.com"    # od posiljalca
    za = "milos.zlatkovic.232.19@ict.edu.rs"    # za primaoca
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
    return

mejl("Poruka za primaoca.")