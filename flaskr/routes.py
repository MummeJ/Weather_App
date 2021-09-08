import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.api_request import get_location, get_weather
from flaskr.forms import SearchForm

bp = Blueprint('routes', __name__, url_prefix='/')

@bp.route('/', methods=['POST', 'GET'])
def index():
    location = get_location()
    current_weather = get_weather(location[0], location[1])
    form = SearchForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            city = form.city.data
            state = form.state.data
            location = form.city.data
            current_weather = get_weather(city, state)
    return render_template('index.html', form=form, location=location, weather=current_weather)
