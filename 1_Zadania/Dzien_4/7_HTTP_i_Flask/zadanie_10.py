from flask import Flask, request

app = Flask(__name__)

@app.route("/tekst", methods=['GET', 'POST'])
def tekst():
    if request.method == 'POST':
        return "wysłałeś POST"
    else:
        return "wysłałeś GET"

if __name__ == '__main__':
    app.run(debug=True)