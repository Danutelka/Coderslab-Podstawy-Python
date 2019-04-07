from random import randint

from flask import Flask

app = Flask(__name__)

@app.route("/random", methods=['GET'])
def licz():
    rnd = [randint(1, 10) for i in range(3)]
    return "wylosowano: %s" % "," .join(str(x) for x in rnd)


if __name__ == "__main__":
    app.run(debug=True)
