from flask import Flask, render_template

flask_app = Flask(__name__)

from app_dir import routes
