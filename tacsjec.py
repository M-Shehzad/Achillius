from flask import Flask, render_template, request, redirect, url_for, session
import requests
from webhook import TacWebhook

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/v1.0")
def v1():
    return render_template("cars/raptorv1.0.html")


@app.route("/v2.0")
def v2():
    return render_template("cars/raptorv2.0.html")


@app.route("/v3.0")
def v3():
    return render_template("")


@app.route("/MechanicalEngineering")
def mech():
    return render_template("departments/mechanical.html")


@app.route("/ElectricalEngineering")
def elec():
    return render_template("departments/electrical.html")


@app.route("/ComputerEngineering")
def cs():
    return render_template("departments/computer.html")


@app.route("/Management")
def mgmt():
    return render_template("departments/management.html")


@app.route("/recruitment", methods=["POST", "GET"])
def recruitment():
    if request.method == "POST":

        wh = TacWebhook()
        wh.addEmbeds(request.form['Name'], request.form['Number'], request.form['Email'], request.form['department'], request.form['CV'], request.form['Linkedin'], request.form['Message'] )
        result = wh.submitWebhook()

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err
        else:
            return render_template('success.html')
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)
