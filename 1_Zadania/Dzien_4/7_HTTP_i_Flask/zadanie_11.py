from flask import Flask, request

app = Flask(__name__)

@app.route("/witaj", methods=['POST', 'GET'])
def witaj():
    if request.method == 'POST':
        a = request.form['imie']
        b = request.form['nazwisko']
        return "Witaj %s %s" %(a, b)
    else:
        return """
        <form method= POST>
                    Imię: <input name='imie'><br>
                    Nazwisko <input name='nazwisko'><br>
                    <button type='submit'>Wyślij!</button>
                </form>
        """
if __name__ == "__main__":
    app.run(debug=True)