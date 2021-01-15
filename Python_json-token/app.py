from flask import Flask, jsonify, request, make_response
import jwt
import json
import datetime

app = Flask(__name__)
PORT = 8080
HOST = "localhost"
app.config['SECRET_KEY'] = "thisisthesecretkey"

@app.route("/unprotected")
def unprotected():
    return ""

@app.route("/protected")
def protected():
    return ""

@app.route("/login")
def login():
    auth = request.authorization    #hvatanje requesta za password i username
    

    if auth and auth.password == "password":    #provera da li je uesena ispravna lozinka
        token = jwt.encode({"user" : auth.username, "exp" : str(datetime.datetime.utcnow() + datetime.timedelta(seconds=30)) }, app.config['SECRET_KEY'],algorithm='HS256') # enkodovanje tokena - | token = jwt.encode({"user" : auth.username, "exp:" : datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}, app.config['SECRET_KEY'],algorithm='HS256') ovo je greska
                                                                                                                                                                #^ potrebno je datetime konvertovati u string
        
        return jsonify({"token":token}) #kreirani tokn - | return jsonify({"token":token.decode()}) ovo je greska

    return make_response("Cloud not verify!", 401, {"WWW-Authenticate":"Basic realm = 'Login required'"})



if __name__ == "__main__":
    app.run(debug=True)