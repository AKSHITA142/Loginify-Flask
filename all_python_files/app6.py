from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/feedback",methods=["POST","GET"])
def feedback():
    if request.method=="POST":
        name=request.form.get("username")
        messege=request.form.get("messege")
        return render_template("thank_you.html",user=name,messege=messege)
    return render_template("feedback.html")