import email
from email.message import EmailMessage
from flask import Flask, render_template, request, redirect, url_for, session
import requests
from flask_compress import Compress
from webhook import TacWebhook
import smtplib
import os
import dotenv

dotenv_file = os.path.join(os.curdir, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
else:
    print('No .env file found')
    exit(0)

EMAIL_ADDRESS = os.environ['email']  # enter sender email's address here
EMAIL_PASSWORD = os.environ['password']   # enter sender email's password here

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
        wh.addEmbeds(request.form['Name'], request.form['Number'], request.form['Email'],
                     request.form['department'], request.form['CV'], request.form['Linkedin'], request.form['Message'])
        result = wh.submitWebhook()

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err
        else:
            if EMAIL_ADDRESS and EMAIL_PASSWORD:
                msg = EmailMessage()
                msg['Subject'] = 'Application Received'
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = request.form['Email']
                msg.add_alternative(render_template(
                    'emailTemplate.html', name=request.form['Name'], department=request.form['department']), subtype='html')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)
            return render_template('success.html')
    else:
        return render_template('form.html')


@app.errorhandler(Exception)
def error404(error):
    return render_template('404.html', content = error.code, stylesheet = "../static/images/IMG_6852.jpg"), error.code


if __name__ == "__main__":
    compress = Compress()
    compress.init_app(app)
    app.run(debug=True)
