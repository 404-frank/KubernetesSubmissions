from flask import render_template
import functions
from time import sleep

def index():
    image_url = functions.get_image_url()
    todo_list = functions.get_todos()
    return render_template("index.html", image_url=image_url, todo_list=todo_list, title="Home")
