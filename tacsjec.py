from flask import Flask, render_template, request, redirect, url_for, session

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

@app.route("/contact-us")
def contactUs():
    return render_template("form.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)