from app_dir import flask_app

@flask_app.route("/")
@flask_app.route("/index")
def home():
    return "<h1>Hello, World</h1>"


@flask_app.route("/about")
def about():
    return "<h1>About Page<h1>"