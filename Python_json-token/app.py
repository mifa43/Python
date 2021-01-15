from flask import Flask, jsonify, request, make_response
import jwt
from functools import wraps
import datetime

app = Flask(__name__)
PORT = 8080
HOST = "localhost"
app.config['SECRET_KEY'] = "thisisthesecretkey"     # vrednos sikret kljuca

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.args.get("token") #ovako treba da izgleda : http://127.0.0.0:5000/route?token=jskij1rkfr39483mfr1
        if not token:
            return jsonify({"Message" : "Token is missing!"}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')  
            print(data)
        except:
            return jsonify({"Message" : "Token is invalid!"}), 403  # http://localhost:5000/protected?token=thisisasecretkey provera da li izuzetak radi
        return f(*args, **kwargs)
    return decorator

@app.route("/unprotected")
def unprotected():
    return jsonify({"Message" : "anyone can view this!"})

@app.route("/protected")
@token_required
def protected():
    return jsonify({"Message" : "This is only availabe for peoples with correct token!"})

@app.route("/login")
def login():
    auth = request.authorization    #hvatanje requesta za password i username
    

    if auth and auth.password == "password":    #provera da li je uesena ispravna lozinka
        token = jwt.encode({"user" : auth.username, "exp" : datetime.datetime.utcnow() + datetime.timedelta(seconds=30) }, app.config['SECRET_KEY'],algorithm='HS256') # enkodovanje tokena - | token = jwt.encode({"user" : auth.username, "exp:" : datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}, app.config['SECRET_KEY'],algorithm='HS256') ovo je greska
                                                                                                                    #nakon isteka vremenskog ogranicenja od 30sec nas token ce postati invalidan ako zelimo ponvo prisup moram da se prijavimo i dobijemo novi token 
        return jsonify({"token": token}) #kreirani tokn - | return jsonify({"token":token.decode()}) ovo je greska

    return make_response("Cloud not verify!", 401, {"WWW-Authenticate":"Basic realm = 'Login required'"})



if __name__ == "__main__":
    app.run(debug=True)