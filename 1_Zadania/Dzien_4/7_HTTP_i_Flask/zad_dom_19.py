from flask import Flask, request

app = Flask(__name__)

@app.route("/kod", methods=['GET', 'POST'])
def kod():
    if request.method == 'POST':

        return "kod pocztowy"
    else:
        return """
        <form method='POST'>
                     Wpisz kod pocztowy:<input name="x"><br>
                     <button type="submit">Zatwierdź</button>
              </form>
        """
if __name__ == "__main__":
    app.run(debug=True)