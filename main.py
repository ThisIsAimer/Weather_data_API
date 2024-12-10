from flask import Flask,render_template

application = Flask(__name__)


@application.route("/")
def home():
    return render_template("home.html")


@application.route("/api/v1/<station>/<date>")
def about(station,date):
    temperature = 23
    # return str(temperature)
    return  {"temp": temperature,"station": station,"date": date}


if __name__ == "__main__":
    application.run(debug=True)
    # application.run(debug=True, port=5001) to change the port number of website