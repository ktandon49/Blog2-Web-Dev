from flask import Flask, render_template, request, g
app = Flask(__name__)

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


