from flask import Flask, request

app = Flask(__name__)

@app.route("/pytanie", methods=['GET','POST'])
def pytanie():
    if request.method == "POST":
        imie = request.form['imie'].upper()
        return "Hello %s !" % imie
    else:
        return "<form method='POST'><input name='imie'>jak masz na imię </form>"

if __name__ == "__main__":
    app.run(debug=True)