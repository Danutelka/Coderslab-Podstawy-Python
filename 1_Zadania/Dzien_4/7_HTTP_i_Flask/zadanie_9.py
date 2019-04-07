from random import randint
from flask import Flask, request

app = Flask(__name__)

@app.route("/zgadywanka", methods=['GET','POST'])
def zgadywanka():
    if request.method == "POST":
        rnd = randint(1, 10)
        guessed = False
        while not guessed:
                numer = request.form['liczba']
        try:
            num = int(numer)
            if num == rnd:
                wynik = "Brawo"
                guessed = True
            elif num >= (rnd -1) and num <= (rnd+1):
                wynik = "Cieplej"
            elif num >= (rnd -2) and num <= (rnd +2):
                wynik = "zimno"
            else:
                wynik ="Pudło"
            return "%s !" %wynik
        except ValueError:
            print("Miałeś wpisać liczbę!")
    else:
            return '''
            <form method='POST'>
                    Wybierz liczbę: <input name='liczba' type='number'> 
                    <button type='submit'>Zgadłeś?</button>
                </form>
                '''

if __name__ == "__main__":
    app.run(debug=True)

