from flask import (Flask, redirect, 
                   url_for, render_template, request)

app = Flask(__name__)

@app.route('/hello/<int:id>')
def hello_world(id):
    print(type(id))
    return "Hello %f" % id

@app.route('/hello/<name>')
def hello_guest(name):
    return "Hello %s" % name

@app.route('/user/<name>')
def hello_user(name):
    if name=="admin":
        return redirect(url_for('hello_world', id=1))
    else:
        return redirect(url_for('hello_guest', name="Guest"))

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        return "Hello %s" % request.form['user']
    return render_template('login.html')

## Recuperer le texte envoyer depuis le champ du texte, et l'afficher dans la meme page HTML

if __name__ == "__main__":
    app.run(debug=True)