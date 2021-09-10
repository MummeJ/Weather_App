import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.api_request import get_location, get_weather
from flaskr.forms import SearchForm

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['POST', 'GET'])
def index():
    location = get_location()
    if location != 'Unavailable':
        current_weather = get_weather(location[0], location[1])
        #form = SearchForm(csrf_enabled=False)
        if request.method == 'POST':
            if form.validate_on_submit():
                city = form.city.data
                state = form.state.data
                city = city.capitalize()
                state = state.upper()
                return redirect('/search/'+city+'_'+state)
        return render_template('index.html', location=location, weather=current_weather)
    else:
        return redirect('/service_unavailable')

@bp.route('/service_unavailable', methods=['GET'])
def unavailable():
    return render_template('unavailable.html')

@bp.route('/search/<city>_<state>', methods=['POST', 'GET'])
def search(city, state):
    try:
        current_weather = get_weather(city, state)
    except:
        flash('Sorry, we could not find the weather for '+city+', '+state+'. Try searching again!')
        return redirect(url_for('routes.index'))
    return render_template('search.html', city=city, state=state, weather=current_weather)
