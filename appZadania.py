# 1-4 Polecenia
from flask import Flask
from flask import url_for
from flask import redirect
from flask import Flask, request
from flask import abort

app = Flask(__name__)

# Zadanie 1
@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć {imie}"

# Zadanie 2
@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"{a} * {b} = {a * b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400 # Kod błędu
    return f"{a} / {b} = {a /b}"

# Zadnaie 3
@app.route("/tabliczka/<int:n>")
def tabela(n):
    if n < 1 or n > 20:
        return "Wpisz w przedziale 1-20"
    wynik = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            wynik += f"{i * j:4}"
        wynik += "\n" 
    return f"<pre>{wynik}</pre>"

# Zadanie 4

@app.route("/produkty")
def produkty():
    # Ustaawiamy że zmienna kat będzie robiła logiczną funkcję z "kat" gdy wpiszemy do linka ?kat= to będziemy mogli dodać/zmienić zawartość na stronie, te "wszystkie" to jest automatyczna wartość.
    kat = request.args.get("kat", "wszystkie")
    sort = request.args.get("sort", "domyślne")
    
    return f"Kategoria: {kat}, sortowanie: {sort}"
# http://localhost:5000/produkty?kat=X&sort=Y
# ?kat=x powoduje to że ,,Kategoria" będzie miała x zamiast wszystkie. Czyli my wybieramy tą kategorię i edytujemy jej zawartość za pomocą linka.
# ,,&" w linkach powoduje to że to jest takie ala ,,i" i dzięki temu możemy edytować drugą zawartość która nam przeszkadza na własną

# Zadanie 5

PRODUKTY = {1: "Produkty", 2: "ogłoszenia", 3: "sale", 4: "Posty", 5: "domena"}

@app.route("/element/<int:id>")
def produkt(id):
    if id not in PRODUKTY:
        abort(404)
    return f"Produkt: {PRODUKTY[id]}"

@app.route("/elementy")
def wszystkie_elementy():
    # Zmienna która jest stringiem i nic nie ma w sobie
    tekst = ""
    # Dla zmiennej ,,nazwa" w Produktach z wartością 
    for nazwa in PRODUKTY.values():
        # Dodaj do zmniennej tekst zawartość nazwa oraz łamanie lini
        tekst += nazwa + "<br>"
        # Zwróć tekst, będzie robił dopuki skończy się for nazwa, czyli wykona polecenie 5 razy.
    return tekst

# Zadanie 6

@app.route("/start")
def stary():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)