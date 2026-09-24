from flask import Flask

app = Flask(__name__)

@app.route("/czesc/<imie>")
def imie(imie):
    return f"Cześć, {imie}"

@app.route("/czesc/<imie>/<int:wiek>")
def imieWiek(imie,wiek):
    return f"Cześć, {imie}, masz {wiek} lat"

@app.route("/dodaj/<int:a>/<int:b>")
def dod(a,b):
    return f"{a} + {b} = {a + b}"

@app.route("/odejmnij/<int:a>/<int:b>")
def min(a,b):
    return f"{a} - {b} = {a - b}"

@app.route("/pomnoz/<int:a>/<int:b>")
def mno(a,b):
    return f"{a} * {b} = {a * b}"

@app.route("/podziel/<int:a>/<int:b>")
def dziel(a,b):
    if a == 0 or b == 0:
        return "Dzielenie przez zero jest nie wykonywalne", 400
    else:
        return f"{a} / {b} = {a / b}"

@app.route("/tabliczka/<int:n>")
def tab(n):
    if n < 1 or n > 20:
        return f"Liczba {n} jest poza zakresem.", 400
    else:
        tekst = ""
        i = 1
        while i <= 20:
            tekst += f"{n} * {i} = {n * i}\n"
            i += 1
        return tekst

if __name__ == "__main__":
    app.run(debug=True)