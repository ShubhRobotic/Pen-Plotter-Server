import asyncio
import os
import subprocess

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

   # async def run_cli():
   # subprocess.run(["/home/pi/UniversalGcodeSender/start-cli.sh","--port /dev/ttyUSB0 --baud 115200 -daemon --controller GRBL"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
   # asyncio.run(run_cli())
    return "<h1>{usr}</h1>"

@app.route("/convert")
def convert():
    return render_template("convert.html")

@app.route("/control")
def control():
    return render_template("control.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
