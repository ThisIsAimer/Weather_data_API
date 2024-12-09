from flask import Flask,render_template

application = Flask("website")

@application.route("/home")
def home():
    return render_template("test.html")

@application.route("/about/")
def about():
    return render_template("about.html")



application.run(debug=True)