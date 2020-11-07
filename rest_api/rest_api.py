import requests

# query = {'lat':'45', 'lon':'180'}   # query za pretraziovanje podataka

resp = requests.post("http://api.open-notify.org/iss-pass.json", data = {'key':'value'}) # web sa koga se uzimaju informacije sa parametrima

print(resp.headers["date"]) # content,text,json  ispisivanje u razlicitim formatima
