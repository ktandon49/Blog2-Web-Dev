from flask import Flask, render_template, request, g
app = Flask(__name__)

import sqlite3

def get_message_db():
    if "message_db" not in g:
        g.message_db = sqlite3.connect("messages_db.sqlite")
    
    g.message_db.execute('CREATE TABLE messages (id INTEGER, handle TEXT, message TEXT)')
    
    return g.message_db

#Base page is linked to base.html
@app.route("/")
def main():
    return render_template("base.html")

@app.route("/submit/", methods=['POST', 'GET'])
def submit():
    if request.method == "GET":
        return render_template("submit.html")
    else:
        #insert_message(request)
        return render_template("submit.html", thanks=True)



@app.route("/view/")
def view():
    return  "Hi there"
#render_template("view.html", rand_messages = random_messages(3))


