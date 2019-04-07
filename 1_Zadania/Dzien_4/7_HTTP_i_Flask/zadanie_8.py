from flask import Flask, request

app = Flask(__name__)

@app.route("/kalkulator", methods=['GET','POST'])
def kalkulator():
    if request.method == "POST":
        if request.form['dzialania'] == 'x':
            wynik = int(request.form['liczba_1']) + int(request.form['liczba_2'])
        elif request.form['dzialania'] == 'y':
            wynik = float(request.form['liczba_1']) - float(request.form['liczba_2'])
        elif request.form['dzialania'] == 'b':
            wynik = float(request.form['liczba_1']) * float(request.form['liczba_2'])
        elif request.form['dzialania'] == 'a':
            wynik = float(request.form['liczba_1']) / float(request.form['liczba_2'])
        return "Wynik wybranego działania %s !" % wynik
    else:
        return '''
         <form method='POST'>
                       Podaj liczbe: <input name='liczba_1'> <br>
                       Podaj drugą liczbę <input name='liczba_2'><br><br>
                       Jakie działanie chcesz wykonać : <br>
                       suma <input type='checkbox' name='dzialania' value ="x"><br>
                       odejmowanie <input type='checkbox' name='dzialania' value="y" ><br>
                       dzielenie <input type='checkbox' name='dzialania' value="a" ><br>
                       mnożenie <input type='checkbox' name='dzialania' value="b"><br><br>
                       <button type='submit'>Pokaż wynik</button>
                   </form>
            '''

if __name__ == "__main__":
    app.run(debug=True)