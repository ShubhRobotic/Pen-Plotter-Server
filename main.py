from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import subprocess
import os
from wtforms.validators import InputRequired
from PIL import Image
import svgutils.transform as sg
import cairosvg


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Gooseberry'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config['GCODE_FOLDER'] = 'static/gcodes'




class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/', methods=['GET', "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        # Get and store file and rename file to Print.jpg
        file = form.file.data
        file.filename = "Print.jpg"
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        img = Image.open('static/files/Print.jpg')
        img_resize_lanczos = img.resize ((200,200), Image.LANCZOS)
        img_resize_lanczos.save('static/files/resized.jpg') 
        cmd1 = ['convert', 'static/files/resized.jpg', 'static/files/Run.svg']
        subprocess.call(cmd1,shell=False)
    return render_template('base.html', form=form)
@app.route('/upload', methods=['GET','POST'])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        # Get and store file and rename file to Print.jpg
        file = form.file.data
        file.filename = "Run.gcode"
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['GCODE_FOLDER'],secure_filename(file.filename)))
    return render_template('convert.html', form=form)

@app.route("/connect/")
def Connect():
    subprocess.run(
        ["/home/pi/my_flask/UI_Buttons_Bash/Connect.sh"], shell=True)
    return redirect('/')

@app.route("/Print/")
def Print():
    subprocess.run(
        ["/home/pi/my_flask/UI_Buttons_Bash/Print.sh"], shell=True)
    return redirect('/')

@app.route("/homing/")
def homing():
    subprocess.run(
        ["/home/pi/my_flask/UI_Buttons_Bash/Homing.sh"], shell=True)
    return redirect('/')

@app.route("/reset_alarm/")
def reset_alarm():
    subprocess.run(
        ["/home/pi/my_flask/UI_Buttons_Bash/Reset_Alarm.sh"], shell=True)
    return redirect('/')


@app.route("/convert")
def convert():
    return render_template("convert.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)