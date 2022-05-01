from flask import Flask, render_template, request, redirect, url_for, session
import pytz
import requests
from datetime import datetime
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
        # url = "https://discord.com/api/webhooks/967857205477007400/UVZEW3zQKIePnbmkLE_EgCK4R6k3XkiVFoesxSZ_yi_JOZTB1uznTlA-Bp4V9FnqB4vl"  # webhook url
        # data = {"content": "",
        #         "username": "Recruitment bot",
        #         "embeds": [
        #             {
        #                 "title": "Recruitment Form",
        #                 "color": 980461,
        #                 "timestamp": str(datetime.now(pytz.timezone('Asia/Kolkata'))),
        #                 "fields": [
        #                     {
        #                         "name": "Name",
        #                         "value": request.form['Name'],
        #                         "inline": False
        #                     },
        #                     {
        #                         "name": "Number",
        #                         "value": request.form['Number'],
        #                         "inline": False
        #                     },
        #                     {
        #                         "name": "Email",
        #                         "value": request.form['Email'],
        #                         "inline": False
        #                     },
        #                     {
        #                         "name": "Interested department:",
        #                         "value": request.form['department'],
        #                         "inline": False
        #                     },
        #                     {
        #                         "name": "CV URL:",
        #                         "value": request.form['CV'] if request.form['CV'] else 'nil',
        #                         "inline": False
        #                     },
        #                     {
        #                         "name": "Linkedin URL:",
        #                         "value": request.form['Linkedin'] if request.form['Linkedin'] else 'nil',
        #                         "inline": False
        #                     },
        #                     {
        #                         "name": "Message",
        #                         "value": request.form['Message'],
        #                         "inline": False
        #                     },
        #                 ]
        #             }
        #         ]}
        # result = requests.post(url, json=data, headers={
        #                        "Content-Type": "application/json"})

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
