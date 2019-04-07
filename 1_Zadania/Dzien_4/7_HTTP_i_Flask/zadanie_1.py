from flask import Flask
app = Flask(__name__)
@app.route("/hello/<imie>")
def hello(imie):
    return "Witaj %s" %imie

if __name__ == "__main__":
    app.run()
