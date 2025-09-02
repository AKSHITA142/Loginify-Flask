from flask import Flask,render_template,request,redirect,flash,url_for,session
from form import RegistrationForm

app=Flask(__name__)
app.secret_key="super-key" 

@app.route("/",methods=["GET","POST"])


def register():
    form=RegistrationForm() #creat object for this class RegistrationForm
    if form.validate_on_submit():
        session["name"]=form.name.data
        session["email"]=form.email.data
        flash(f"Welcome,{session["name"]}! You are Registered SuccessFully")
        return redirect(url_for("success"))
    return render_template("Registration.html",form=form)

@app.route("/success")
def success():
    form=RegistrationForm() #creat object for this class RegistrationFor
    return render_template("thank_you_res.html",user=session["name"])
