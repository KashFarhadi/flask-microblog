from flask import render_template
from app_dir import flask_app

@flask_app.route("/")
@flask_app.route("/index")
def home():
    return render_template('base.html')



@flask_app.route("/about")
def about():
    return ""