from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import subprocess
import os
from wtforms.validators import InputRequired
from PIL import Image


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Gooseberry'
app.config['UPLOAD_FOLDER'] = 'static/files'


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
        # resize image using 
        img = Image.open('./static/files/Print.jpg') # Open image
        img = img.resize((150, 100)) # Resize image
        img.save('./static/files/foo.jpg') # Save resized image
    return render_template('base.html', form=form)

@app.route("/homing/")
def homing():
    subprocess.run(
        ["/home/pi/my_flask/UI_Buttons_Bash/Homing.sh"], shell=True)
    return render_template('Control.html')

@app.route("/reset_alarm/")
def reset_alarm():
    subprocess.run(
        ["/home/pi/my_flask/UI_Buttons_Bash/Reset_Alarm.sh"], shell=True)
    return render_template('Control.html')


@app.route("/convert")
def convert():
    return render_template("convert.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)