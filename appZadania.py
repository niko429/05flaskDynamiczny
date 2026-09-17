# 1-4 Polecenia
from flask import Flask

app = Flask(__name__)

# Zadanie 1
@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć {imie}"

if __name__ == "__main__":
    app.run(debug=True)