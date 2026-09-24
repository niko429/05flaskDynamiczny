from flask import Flask

app = Flask(__name__)

@app.route("/czesc/<imie>")
def imie(imie):
    return f"Cześć {imie}"

if __name__ == "__main__":
    app.run(debug=True)