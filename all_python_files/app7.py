from flask import Flask,render_template,request,redirect,flash,url_for

app=Flask(__name__)
app.secret_key="super-key"

@app.route("/",methods=["POST","GET"])
def form():
    if request.method=="POST":
        name=request.form.get("username")
        if not name:
            flash("Name cannot be empty")
            return redirect(url_for("form"))
        flash(f"Thanks {name} your feedback was saved")
        return render_template("thank_you.html",user=name)
    return render_template("feedback.html")

# @app.route("/thankyou")
# def thankyou():
#     return render_template("thank_you.html")