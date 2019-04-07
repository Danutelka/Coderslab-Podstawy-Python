
from flask import Flask, request

app = Flask(__name__)

@app.route("/totek", methods=['GET'])
def licz():
    a = list(range(1,50))
    shuffle(a)
    return "3 losowe liczby: %s" % "," .join(str(x) for x in a[:6])


if __name__ == "__main__":
    app.run(debug=True)