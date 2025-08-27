#flask is only looks into templates folder for html file so pay attention to the spellings
#in this tuto i leart that how html files are connect by template folder

from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")