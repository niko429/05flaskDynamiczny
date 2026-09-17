# 1-4 Polecenia
from flask import Flask

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
        return "Nie dzielimy przez zero", 400
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

if __name__ == "__main__":
    app.run(debug=True)