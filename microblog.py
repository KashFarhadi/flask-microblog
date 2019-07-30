from app_dir import flask_app
from app_dir.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    flask_app.run(debug=True)
