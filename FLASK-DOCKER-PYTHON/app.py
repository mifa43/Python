from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3200
HOST = "0.0.0.0"

INFO = {
    "jezici":{
        "es":"Spanija",
        "en":"Engleska",
        "fr":"Francuska",
    },
    "boje":{
        "r":"crvena",
        "g":"zelena",
        "b":"plava",
    },
    "clouds":{
        "IBM":"IBM CLOUD",
        "AMAZON":"AWS",
        "MICROSOFT":"AZURE",
    }
}
        #GET METODA
@app.route("/")
def home():
    return "<h1 style='color:blue'>Ovo je pocetna!!!</h1>"

@app.route("/temp")
def template():
    return render_template("index.html")

# localhost:3200/qstr?name=EP&age=25
#                    ^ nakon upitnika ide key = value u ovom slucaju ime = ep & godine = 25               
@app.route("/qstr")
def query_string():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res

    res = make_response(jsonify({"error":"nema query stringa"}),400)
    return res
#   PRIKAZ JSON 
@app.route("/json")
def get_json():
    res = make_response(jsonify(INFO),200)
    return res

#pretrazivanje kolekcija i clanova
#localhost:3200/json/clouds/IBMs = 400 greska ne postoji ovaj clan
#localhost:3200/json/clouds/IBM = 200 postoji clan
@app.route("/json/<collection>/<member>")
def get_data(collection, member):
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify({"res":member}),200)
            return res

        res = make_response(jsonify({"error":"clan nije pronadjen"}),400)   # greska ako nema clana
        return res

    res = make_response(jsonify({"error":"kolekcija nije pronadjen"}),400)  # gresk ako nema kolekcije
    return res

#POST METODA
#kreiranje nove kolekcije localhost:3200/json/cars = naziv cars, prvo se namesta POST METODA, otvaramo body, raw.
#zatim se kreira json struktura u body i upisuju vrednosti kada odemo da proverimo u postmanu localhost:3200/json = vidimo novu kolekciju cars

@app.route("/json/<collection>", methods = ["POST"])
def create_collection(collection):
    req = request.get_json()

    if collection in INFO:
        res = make_response(jsonify({"error":"Kolekcija vec postoji"}))
        return res

    INFO.update({collection: req})
    res = make_response(jsonify({"poruka":"Kolekcija je kreirana!"}))
    return res

#PUT METODA
# localhost:3200/json/cars/f - body/raw kada obrisemo clanove i dodamo {"novi":"ford"} na taj nacin smo izmenili clana ferrari sa fordom
@app.route("/json/<collection>/<member>", methods = ["PUT"])
def update_collection(collection, member):

    req = request.get_json()

    if collection in INFO:
        if member:
            INFO[collection][member] = req["novi"]
            res = make_response(jsonify({"res":INFO[collection]}),200)
            return res

    
        res = make_response(jsonify({"error":"Clan nije pronadjen"}),400)
        return res

    res = make_response(jsonify({"error":"Kolekcija nije pronadjena"}),400)
    return res

#DELETE METODA
# u postmanu se odabere delete metoda localhost:3200/json/cars ukucamo i brisemo kolekciju cars 
# ali prethodno je potrebno da kolekcija cars postoji. Potrebno je da se vratimo na post metodu i kreiramo cars 


@app.route("/json/<collection>", methods = ["DELETE"])
def delete_collection(collection):
    if collection in INFO:
        del INFO[collection]
        res = make_response(jsonify(INFO),200)
        return res

    res = make_response(jsonify({"error":"Kolekcija nije pronadjena"}),400)
    return res

if __name__ == "__main__":
    print("Server je pokrenut na portu %s"%(PORT))
    app.run(host = HOST, port = PORT)


# VIRTUALENV
#1. prvo se instalira sa pip install virtuelenv
#2. virtualenv -p python docker-flask
#3. cd c:/put do direktorijuma u kome se nalazi novo kreirani virtualenv | docker-flask
#4. cd scripts
#5. cmd activate | ispisuje poruku neku vezanu za microsoft =Microsoft Windows [Version 10.0.19042.685](c) 2020 Microsoft Corporation. All rights reserved.
#6. nakon toga kada ukucamo activate je ispisano sivom bojom i opalimo enter
#7. nas virtuelenv je aktivan ovako izgleda kada je aktivan: (docker_flask) C:\Users\mifa4\Desktop\Python\Python_pro\Python\FLASK-DOCKER-PY