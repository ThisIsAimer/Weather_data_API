from flask import Flask,render_template
import numpy
import pandas

application = Flask(__name__)

stations = pandas.read_csv("dataAnalysisWithJupyter/data_small/stations.txt",skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

@application.route("/")
def home():
    return render_template("home.html", data = stations.to_html())

@application.route("/api/v1/<station>")
def one_station(station):
    filename = "dataAnalysisWithJupyter/data_small/TG_STAID"+str(station).zfill(6)+".txt"
    data = pandas.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    data["   TG"] = data["   TG"].mask(data["   TG"] == -9999,numpy.nan)
    data["TEMP"] = data["   TG"] / 10
    data = data[["    DATE","TEMP"]].dropna()
    return render_template("oneStation.html", data= data.to_html())

@application.route("/api/v1/yearly/<station>/<date>")
def one_year(station,date):
    filename = "dataAnalysisWithJupyter/data_small/TG_STAID"+str(station).zfill(6)+".txt"
    f_data = pandas.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    f_data["str date"]= f_data ["    DATE"].astype(str)
    f_data = f_data[f_data ["str date"].str.startswith(str(date))]
    f_data["TEMP"] = f_data["   TG"] / 10
    f_data = f_data[["    DATE","TEMP"]]
    return render_template("oneStation.html", data=f_data.to_html())




@application.route("/api/v1/<station>/<date>")
def station_date(station,date):
    filename = "dataAnalysisWithJupyter/data_small/TG_STAID"+str(station).zfill(6)+".txt"
    data = pandas.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    data["    DATE"] = data["    DATE"].mask(data["    DATE"] != date, numpy.nan)
    data["   TG"] = data["   TG"].mask(data["   TG"] == -9999, numpy.nan)
    data["TEMP"] = data["   TG"]/10
    data = data[["    DATE","TEMP"]].dropna()
    return  render_template("oneStation.html",data= data.to_html())


if __name__ == "__main__":
    application.run(debug=True)
    # application.run(debug=True, port=5001) to change the port number of website