from flask import Flask,render_template
import pandas

application = Flask(__name__)


@application.route("/")
def home():
    return render_template("home.html")


@application.route("/api/v1/<station>/<date>")
def about(station,date):
    filename = "dataAnalysisWithJupyter/data_small/TG_STAID"+str(station).zfill(6)+".txt"
    data = pandas.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temp = data.loc[data["    DATE"] == date] ["   TG"].squeeze() / 10
    # return str(temperature)
    return  {"temp": temp,"station": station,"date": date}


if __name__ == "__main__":
    application.run(debug=True)
    # application.run(debug=True, port=5001) to change the port number of website