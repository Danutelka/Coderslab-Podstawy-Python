from flask import Flask, request
import math

app = Flask(__name__)

@app.route("/n", methods=('GET', 'POST'))
def n():
    if request.method == "POST":
        liczba = int(request.form['x'])
        a = 2 ** liczba
        b = liczba ** liczba
        c = math.factorial(liczba)
        return "Tabelka %s %s %s" %(a, b, c)
    else:
        return """
        <form method='POST'>
                    Wpisz liczbę naturalną: <input name='x'><br>
                    <button type='submit'>Zatwierdź</button>
                </form>
        """

if __name__ == "__main__":
    app.run(debug=True)

