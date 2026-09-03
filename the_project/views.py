from flask import render_template
import functions

def index():

    image_url = functions.get_image_url()
    todo_list = ["this is the first todo", "this is the second one", "and this keeps on going..."]
    return render_template("index.html", image_url=image_url, todo_list=todo_list, title="Home")
