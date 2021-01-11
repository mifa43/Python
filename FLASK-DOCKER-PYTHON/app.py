from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3200
HOST = "0.0.0.0"

info = {
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

if __name__ == "__main__":
    print("Server je pokrenut na portu %s"%(PORT))
    app.run(host = HOST, port = PORT)
