from flask import Flask

app = Flask(__name__)

@app.route("/czesc/<imie>")
def imie(imie):
    return f"Cześć, {imie}"

@app.route("/czesc/<imie>/<int:wiek>")
def imieWiek(imie,wiek):
    return f"Cześć, {imie}, masz {wiek} lat"

if __name__ == "__main__":
    app.run(debug=True)