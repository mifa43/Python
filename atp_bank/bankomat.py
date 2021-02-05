from flask import Flask, request, jsonify, make_response
from flask_mysqldb import MySQL
import os
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import uuid
from werkzeug.security import generate_password_hash, check_password_hash 
import jwt
import datetime
from functools import wraps
from PIL import Image
import random

app = Flask(__name__)

dbpass = os.getenv('dbpassword')
app.config['SECRET_KEY'] = "ovojemojtajnikljuc"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = dbpass
app.config['MYSQL_DB'] = 'rest_api'

db = MySQL(app)
app.app_context().push()

class Insert_bank():    # kreiranje korisnika i upisivanje u bazu 
    def __init__(self, ime, prezime, public_id, password, is_admin):
        
        self.ime = ime
        self.prezime = prezime
        self.public_id = public_id
        self.password = password
        self.is_admin = is_admin
        cur = db.connection.cursor()
        query = "INSERT INTO rest_api.banka_user (ime, prezime, public_id, password, is_admin) VALUES ('{0}','{1}','{2}','{3}','{4}');".format( self.ime, self.prezime, self.public_id, self.password, self.is_admin)
        cur.execute(query)
        db.connection.commit()
        cur.close()

class Make_qr():    # generisanje qr koda sa informacijama o korisniku 
    def __init__(self, public_id, password, name_qr):
        self.public_id = public_id
        self.password = password
        self.name_qr = name_qr
        self.qr = pyqrcode.create(self.public_id + " " + self.password)
        self.qr.png(self.name_qr + ".png", scale = 9)

class Insert_qr():    # kreiranje korisnika i upisivanje u bazu 
    def __init__(self, public_id, pin):
        self.public_id = public_id
        self.pin = pin

        cur = db.connection.cursor()
        query = "INSERT INTO rest_api.qr_user (public_id, pin) VALUES ('{0}', {1});".format(self.public_id, self.pin)
        cur.execute(query)
        db.connection.commit()
        cur.close()

def token_required(f):  # dekorater koji kada je pozvan zahteva od korisnika token. u ovom bloku token se dekoduje i vracamo public_id u variablu key nakon toga je upisujemo kao parametar u root definicijama i pravimo proveru da li je admin
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')

            cur = db.connection.cursor()
            query = "SELECT public_id FROM rest_api.banka_user WHERE public_id='{0}';".format(data['public_id'])
            cur.execute(query)
            var = cur.fetchall()
            db.connection.commit()
            cur.close()
            for key in var:
                key
                print(key[0])
        except:
            return jsonify({'message' : 'token is invalid!'})
        return f(key, *args, **kwargs)
    return decorated

@app.route("/user/<public_id>", methods = ['GET'])
@token_required
def get_one_user(key, public_id):    # metoda get nam vraca jednog korisnika ciji je id unesen u path = localhost:5000/user/c665e326-344f-44dd-9056-c112a125229e
    for user in key:
        cur = db.connection.cursor()
        query = "SELECT is_admin FROM rest_api.banka_user WHERE public_id = '{0}';".format(user)
        cur.execute(query)
        var = cur.fetchall()
        db.connection.commit()
        cur.close()
        cur = db.connection.cursor()

        for item in var:

            if item[0] == 0:

                return jsonify({'message' : 'Cannot preform that function!'})

    cur = db.connection.cursor()
    query = "SELECT id_user, ime, prezime, public_id, password, is_admin FROM rest_api.banka_user WHERE public_id='{0}';".format(public_id)
    cur.execute(query)
    db.connection.commit()
    cur.close()

    for i in cur:   # vracamo podatke iz baze u json formatu
        user_data = {}
        user_data['id_user'] = i[0]
        user_data['ime'] = i[1]
        user_data['prezime'] = i[2]
        user_data['public_id'] = i[3]
        user_data['password'] = i[4]
        user_data['is_admin'] = i[5]
        
    try:
        return jsonify({"Users": user_data})
    except:
        return jsonify({"Message" : "User not found"})

@app.route("/user", methods = ['POST'])
@token_required
def create_user(key):  # post metoda za kreiranje korisnika requestujemo json format i upisujemo lozinku npr 123-i enkodujemo u hash password unosimo i ime i prezime korisnika u bazu
    for user in key:
        cur = db.connection.cursor()
        query = "SELECT is_admin FROM rest_api.banka_user WHERE public_id = '{0}';".format(user)
        cur.execute(query)
        var = cur.fetchall()
        db.connection.commit()
        cur.close()
        cur = db.connection.cursor()

        for item in var:

            if item[0] == 0:

                return jsonify({'message' : 'Cannot preform that function!'})
    
    
    data = request.get_json()

    hash_password = generate_password_hash(data['password'], method = 'sha256')

    Insert_bank(data['name'], data['lastname'], str(uuid.uuid4()), hash_password, data['is_admin'])

    return jsonify({"message" : "New user is created"})

@app.route("/createQR", methods = ['POST'])
@token_required
def generate(key): # generisanje qr koda i unosenje podataka korisnika (lozinka i javni id) ovo ce posle biti provera za stanje na qr kodu 
    for user in key:
        cur = db.connection.cursor()
        query = "SELECT is_admin FROM rest_api.banka_user WHERE public_id = '{0}';".format(user)
        cur.execute(query)
        var = cur.fetchall()
        db.connection.commit()
        cur.close()
        cur = db.connection.cursor()

        for item in var:

            if item[0] == 0:

                return jsonify({'message' : 'Cannot preform that function!'})
    
    data = request.get_json()

    cur = db.connection.cursor()
    query = "SELECT public_id, password FROM rest_api.banka_user WHERE public_id='{0}' and password = '{1}';".format(data['public_id'], data['password'])
    cur.execute(query)
    var = cur.fetchall()
    db.connection.commit()
    cur.close()

    if not var:
        return jsonify({"message" : "no user found"})

    rand_num = "0123456789"

    p = (random.choice(rand_num)for i in range(4))
    p = "".join(p)

    Make_qr(data['public_id'],data['password'], data['name_qr'])
    Insert_qr(data['public_id'], p) # kreiranje qr_koda u bazi 
    return jsonify({"message" : "QR-code is generated"})

# GET - provera stanja
# PUT - uplacivanje i podizanje

@app.route("/bank_machine/<qr_data>/<pin>", methods = [ 'GET',  'PUT'])
def decode_qr(qr_data, pin): # dekodovanje qr koda u putanju unosimo ime qr-koda npr(3.png) nakon toga ide pin
    info = '''
    How to pay? : Set the method to "PUT", in the URL after localhost: 5000 / decode / enter the name of your QR code / the next value represents pin 1234. eg (localhost: 5000 / decode / qr.png / 1111).
        Select Body >>> raw >>> json and enter {"method": "pay", "value": 5000}

    How to width? : Set the method to "PUT", enter the name of your qr code and pin..
        Select Body >>> raw >>> json and enter {"method": "width", "value": 2700}

    How to check the status? : Set the method to "GET", enter the name of your qr code and pin.
        Select Body >>> raw >>> json and enter {"method": "status"}
    '''
    print(info)
    try:    # ako nema te slike dizemo izuzetak
        img = decode(Image.open("C:/Users/mifa4/Desktop/Python/Python_pro/Python/" + qr_data))
        
        for item in img[0].data.decode('ascii'):
            if item == " ":
                data = img[0].data.decode('ascii')
                myset = " ".join(data)
                myset = data.split(" ")
                h = {}
                h["public_id"] = myset[0]
                h["password"] = myset[1]
                cur = db.connection.cursor()
                query = "SELECT public_id, password FROM rest_api.banka_user WHERE public_id='{0}' and password = '{1}';".format(h['public_id'], h['password']) # provera da li je id iz qr.png postojeci u bazi
                cur.execute(query)
                var = cur.fetchall()
                db.connection.commit()
                cur.close()
    
                if not var:
                    return jsonify({"message" : "no user found with current qr-code"})  #ako nema qr-koda znci da korisnik ne pripada nasoj bazi
                for item in var:
                    
                    cur = db.connection.cursor()
                    query = "SELECT public_id FROM rest_api.qr_user WHERE public_id='{0}';".format(h['public_id'])  # provera id-a da li postoji u qr_user bazi
                    cur.execute(query)
                    var1 = cur.fetchall()
                    db.connection.commit()
                    cur.close()
                    for i in var1:
                        if h['public_id'] == item[0] and h['public_id'] == i[0]:
                            
                            cur = db.connection.cursor()
                            query = "SELECT pin FROM rest_api.qr_user WHERE pin = '{0}';".format(pin)   # provera da li je pod time id-om tacan uneseni pin
                            cur.execute(query)
                            var2 = cur.fetchall()
                            db.connection.commit()
                            cur.close()
                           
                            if not var2:
                                return jsonify({"Message" : "invalid pin"})
                            for j in var2:
                                if j[0] == pin:
                                    data = request.get_json()

                                    if request.method == 'GET':     # get metodu koristimo za proveru stanja sa qr_koda
                                        if data['method'] == 'status':  # u postmanu navodimo 'GET' metodu u json formatu sa {"method" : "status"} ovako izgleda putanja localhost:5000/decode/aleksandar_qr.png/3897 prva vrednost posle decode je ime slike qr_koda nakon toga je pin
                                            
                                            cur = db.connection.cursor()
                                            query = "SELECT sredstva FROM rest_api.qr_user WHERE pin = '{0}' and public_id = '{1}';".format(pin, h['public_id'])    # selektujemo sredstva na osnovu id-a i pin-a
                                            cur.execute(query)
                                            var3 = cur.fetchall()
                                            db.connection.commit()
                                            cur.close()
                                            for s in var3:
                                                
                                                return jsonify({'your balance' : s[0]}) # ispisivanje sredstva
                                        else:
                                            return jsonify({'message' : 'wrong method'})
                                                                        
                                    if request.method == 'PUT':     # kada je metod 'PUT' dodajemo dve pod metode {"method" : "width", "value" : 3000} vrednost koju dizemo sa racuna 
                                        if data['method'] == 'width':
                                            
                                            cur = db.connection.cursor()
                                            query = "SELECT sredstva FROM rest_api.qr_user WHERE pin = '{0}' and public_id = '{1}';".format(pin, h['public_id'])
                                            cur.execute(query)
                                            var3 = cur.fetchall()
                                            db.connection.commit()
                                            cur.close() 
                                            
                                            for value in var3:
                                                
                                                x = int(value[0] - data['value'])

                                                if value[0] == 0:
                                                    return jsonify({"Message" : "there are not enough funds available"})
                                                if x <= -1:
                                                    return jsonify({"Message" : "there are not enough funds available 1 "})
                                              
                                                cur = db.connection.cursor()
                                                query = "UPDATE rest_api.qr_user SET sredstva = '{0}' WHERE pin = '{1}'".format(int(x), pin)
                                                cur.execute(query)
                                                db.connection.commit()
                                                cur.close()                                              
                                                
                                                return jsonify({"You are width" : data['value']})
                                        
                                        elif data['method'] == 'pay':   #{"method" : "pay", "value" : 3000} uplacujemo na racun
                                                                                       
                                            cur = db.connection.cursor()
                                            query = "SELECT sredstva FROM rest_api.qr_user WHERE pin = '{0}' and public_id = '{1}';".format(pin, h['public_id'])
                                            cur.execute(query)
                                            var3 = cur.fetchall()
                                            db.connection.commit()
                                            cur.close() 
                                            
                                            for value in var3:
                                                
                                                x = int(value[0] + data['value'])
                                             
                                                cur = db.connection.cursor()
                                                query = "UPDATE rest_api.qr_user SET sredstva = '{0}' WHERE pin = '{1}'".format(int(x), pin)
                                                cur.execute(query)
                                                db.connection.commit()
                                                cur.close()                                             
                                                
                                                return jsonify({"You are pay" : data['value']})
                                           
                                
        return jsonify({"message" : "wrong method"})
    except: 
        return jsonify({"message" : "No such qr.png"})

@app.route("/login")    # ruta za logovanje ako su uneseni podaci validni dobicemo token sa korisnickim public_id-om nakon toga pravimo proveru da li je admin
def login():            # blokovima za generisanje,kreiranje korisnika,pretrazivanje ima pristup samo admin
    auth = request.authorization

    cur = db.connection.cursor()
    query = "SELECT ime FROM rest_api.banka_user WHERE ime = '{0}';".format(auth.username)
    cur.execute(query)
    var = cur.fetchall()
    db.connection.commit()
    cur.close()

    if not auth or not auth.username or not auth.password:
        return make_response("could not verify 0", 401, {'WWW-Authenticate' : 'Basic realm = "Login required"'})
    
    for user in var:
        user = "".join(user)
        if auth.username == user:
            cur = db.connection.cursor()
            query = "SELECT password FROM rest_api.banka_user WHERE ime = '{0}';".format(auth.username)
            cur.execute(query)
            var = cur.fetchall()
            db.connection.commit()
            cur.close()
            for password in var:
                password = "".join(password)
                if check_password_hash(password, auth.password):
                    cur = db.connection.cursor()
                    query = "SELECT public_id FROM rest_api.banka_user WHERE password = '{0}';".format(password)
                    cur.execute(query)
                    var = cur.fetchall()
                    db.connection.commit()
                    cur.close()
                    for public_id in var:
                        public_id = "".join(public_id)
                        token = jwt.encode({"public_id" : public_id, "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'], algorithm='HS256')
                        # token ima tajmer 30minuta nakon toga vise nije validan
                        
                        return jsonify({"Token" : token})

    if not var:
        return make_response("could not verify 1", 401, {'WWW-Authenticate' : 'Basic realm = "Login required"'})
    return make_response("could not verify 2", 401, {'WWW-Authenticate' : 'Basic realm = "Login required"'})
if __name__ == "__main__":
    app.run(debug = True)

#admin 12345, milena soba1

#sledeci korak je srediti izbacivanje greski, dodati deo gde ne mozemo da odemo u minus, srediti pravopis i dodati upuctvo upotrebe