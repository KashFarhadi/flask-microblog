from flask import render_template
from app_dir import flask_app


@flask_app.route("/")
@flask_app.route("/index")
def home():

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('base.html', posts=posts)


@flask_app.route("/about")
def about():
    return "<h1>About Page </h1>"
