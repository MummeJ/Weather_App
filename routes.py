from app import app, db
#from app import login_manager
from flask import request, render_template, flash, redirect, url_for
#from models import User, DinnerParty
from flask_login import current_user, login_user, logout_user, login_required
#from forms import RegistrationForm,LoginForm, DinnerPartyForm, RsvpForm
from werkzeug.urls import url_parse

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
