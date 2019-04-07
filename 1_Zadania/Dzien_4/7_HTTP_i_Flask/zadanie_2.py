from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route("/czas")
def czas():
    return "aktualny czas to: %s" % datetime.now()

if __name__ == "__main__":
    app.run(debug=True)