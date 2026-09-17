# 1-4 Polecenia
from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "Działa"

@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć, {imie}"

@app.route("/uzytkownik/<imie>/<nazwisko>")
def uzytkownik(imie, nazwisko):
    return f"Użytkownik, {imie} {nazwisko}"

@app.route("/produkt/<int:id>")
def produkt(id):
    return f"Produkt numer {id}, typ: {type(id).__name__}"

@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a /b}"

# Polecenie 5
from flask import Flask, request

@app.route("/powitanie")
def powitanie():
    imie = request.args.get("imie", "nieznajomy")
    godzina = request.args.get("godzina", type=int)
    if godzina is not None and godzina < 12:
        return f"Dzień dobry, {imie}"
    return f"Witaj, {imie}!"

# Polecenia 6
# Polecenie 6.1
from flask import url_for

@app.route("/linki")
def linki():
    return url_for("produkt", id=5)

# Polecenie 6.2
from flask import redirect

@app.route("/stary-adres")
def stary():
    return redirect(url_for("index"))

# Polecenie 6.3
from flask import abort

PRODUKTY = {1: "Laptop", 2: "Mysz", 3: "Klawiatura"}

@app.route("/produkt/<int:id>")
def produkt(id):
    if id not in PRODUKTY:
        abort(404)
    return f"Produkt: {PRODUKTY[id]}"

if __name__ == "__main__":
    app.run(debug=True)