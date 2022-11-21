from flask import Flask, redirect, url_for, render_template, request, Response, flash
import requests
import os
import asyncio
import subprocess
import sys

app = Flask(__name__)

# async def run_cli():
# subprocess.run(["/home/pi/UniversalGcodeSender/start-cli.sh","--port /dev/ttyUSB0 --baud 115200 -daemon --controller GRBL"])
# if request.method == 'POST':
#  if request.form.get['submit_button'] == 'Connect':
#
#  elif request.form.get['submit_button'] == 'Home':
#     subprocess.call(["/home/pi/my_flask/UI_Buttons_Bash/Homing.sh"], shell=True)
#  else:
#        pass # unknown
#  elif request.method == 'GET':


@app.route('/')
def home():
    return render_template('base.html')


@app.route("/control/", methods=['POST'])
def control():
    if request.method == 'POST':
        subprocess.run(
            ["/home/pi/my_flask/UI_Buttons_Bash/Connect.sh"], shell=True)
    return "render_template('base.html')"


@app.route("/convert")
def convert():
    return render_template("convert.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
