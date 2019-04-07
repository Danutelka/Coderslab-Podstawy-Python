from flask import Flask, request

app = Flask(__name__)

@app.route("/licz/<int:liczba1>/<int:liczba2>", methods=['GET'])
def licz(liczba1, liczba2):
    a = liczba1 + liczba2
    return "suma liczb: %s" %a

if __name__ == "__main__":
    app.run(debug=True)

