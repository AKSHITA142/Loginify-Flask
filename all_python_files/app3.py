#flask is only looks into templates folder for html files so pay attention to the spellings

from flask import Flask,render_template,request,session,Response

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/submit" ,methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    
    # if username=="AKSHITA" and password=="142":
    #     # session["user"]=username
    #     return render_template("welcome.html",name=username)
    # else:
    #     return Response("Invalid Candidate",mimetype="text/HTML")
    
    #Now in the backend if i want to check from the dict for valid username and password then i have to creat dict
    valid_users={
        "admin":"123",
        "Akshita":"142",
        "Shreya":"765"
    }
    
    if username in valid_users and password==valid_users[username]:
        return render_template("welcome.html",name=username)
    else:
        return Response("Invalid Candidate",mimetype="text/plain")