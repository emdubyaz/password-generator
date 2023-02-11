import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('entry.html', the_title = "Password Generator")

@app.route('/password', methods=["GET","POST"])
def create_password():
    if request.method == "POST":

        l = int(request.form.get("password_length"))
        password = " "

        for i in range(l):
            select = random.randint(1,3)
            if select == 1:
                password += str(random.randint(0,9))
            elif select == 2:
                password += random.choice(string.ascii_letters)
            elif select == 3:
                password += random.choice(string.punctuation)

        return render_template("entry.html",password=password)


app.run()
        