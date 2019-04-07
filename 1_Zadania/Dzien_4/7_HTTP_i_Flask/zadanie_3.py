from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route("/data")
def data():
    return "aktualna data to: %s" % datetime.now().strftime("%A:%B:%Y")

if __name__ == "__main__":
    app.run(debug=True)