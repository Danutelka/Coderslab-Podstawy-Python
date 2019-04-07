from flask import Flask, request

import requests

app = Flask(__name__)
@app.route("/hello/<imie>")
def hello(imie):
    return "Witaj %s" %imie

@app.route("/hello_post/", methods =['GET','POST'])
def hello_post():
    if request.method == "POST":
        return "hello from the post"
    else:
        return "<form method='POST'><button type='submit'>postnij</button></form>"

@app.route("/otworz_stronke/<path:url>/")
def otworz_stronke(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    app.run()
