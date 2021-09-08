import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.api_request import get_location, get_weather

bp = Blueprint('routes', __name__, url_prefix='/')

@bp.route('/', methods=['POST', 'GET'])
def index():
    location = get_location()
    current_weather = get_weather(location[0], location[1])
    #return render_template('index.html',location=location, #weather=current_weather)
    return render_template('index.html', location=location, weather=current_weather)
