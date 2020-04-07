from urllib.request import urlopen
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, IntegerField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'


class ReusableForm(Form):
    url = TextField('url', validators=[validators.DataRequired()])


def url_to_image(url, readFlag=cv2.IMREAD_GRAYSCALE):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)
    return image


model = tf.keras.models.load_model("64x3-CNN.model")


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        if form.validate():
            url = request.form['url']

            img = url_to_image(url)
            img_size = 150
            img = cv2.resize(img, (img_size, img_size))

            x = np.array(img).reshape(-1, img_size, img_size, 1)
            x = x/255

            categories = ["Šuo", "Katė"]
            prediction = model.predict_classes([x])

            flash(categories[int(prediction[0][0])])
        else:
            flash('Neįvedėte URL!')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()
