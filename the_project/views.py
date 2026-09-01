from flask import render_template
import functions

def index():
    image_url = functions.get_image_url()
    return render_template("index.html", image_url=image_url, title="Home")
