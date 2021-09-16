import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
from flaskr.api_request import get_location, get_current_weather, get_future_weather
from flaskr.forms import SearchForm
from datetime import datetime, date, timedelta

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['POST', 'GET'])
def index():
    daily_dates = []
    d = date.today()
    location = get_location()
    if location != 'Unavailable':
        for num in range(1, 8):
            daily_dates.append(str(d.day))
            d = d + timedelta(days=num)
        current_weather = get_current_weather(location[0], location[1])
        hourly_weather, daily_weather = get_future_weather(location[0], location[1])
        form = SearchForm(csrf_enabled=False)
        if request.method == 'POST':
            if form.validate_on_submit():
                input = form.search_bar.data.split(', ')
                city = input[0]
                state = input[1]
                city = city.capitalize()
                state = state.upper()
                return redirect('/search/'+city+'_'+state)
        return render_template('index.html', form=form, location=location, current_weather=current_weather, hourly_weather=hourly_weather, daily_weather=daily_weather, daily_dates=daily_dates)
    else:
        return redirect('/service_unavailable')

@bp.route('/service_unavailable', methods=['GET'])
def unavailable():
    form = SearchForm(csrf_enabled=False)
    return render_template('unavailable.html', form=form)

@bp.route('/search/<city>_<state>', methods=['POST', 'GET'])
def search(city, state):
    form = SearchForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            input = form.search_bar.data.split(', ')
            city = input[0]
            state = input[1]
            city = city.capitalize()
            state = state.upper()
            return redirect('/search/'+city+'_'+state)
    try:
        current_weather = get_current_weather(city, state)
    except:
        flash('Sorry, we could not find the weather for '+city+', '+state+'. Try searching again!')
        return redirect(url_for('routes.index'))
    return render_template('search.html', form=form, city=city, state=state, weather=current_weather)
