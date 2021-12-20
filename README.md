# Weather App

## ==Description== ##
This is weather app that makes an api call to openweathermap.com to get the weather data. It automatically finds your current location by using the Python geocoder module. When you search for a location, An api call is made to the google geocode api to convert city and state text into coordinates. These coordinates are then used to make an api call to openweathermap.com to get the weather data for that location. 

### ==Files and directories== ###
   - `flaskr` - Main application directory.
      - `static` - Contains all static files.
         - `css` - Contains main.css
         - `js` - Contains main.js
      - `template` - Contains all html files for the app.
         - `base.html` - The base template that all other templates extend.
         - `search.html` - Search page.
         - `Unavailable.html` - Unavailable page.
         - `index.html` - Main template or "homepage".
      - `__init__.py` - File that creates an instance of Flask app.
      - `api_request.py` - File containing all api requests.
      - `db.py` - Creates database.
      - `forms.py` - Contains all the forms.
      - `routes.py` - Contains all of the routes.
      - `schema.sql` - Creates the sql table schema.

### ==Executing Program== ###
To run, set the following environment variables:
* Powershell
	* `$env:FLASK_APP = "flaskr"`
	* `$env:FLASK_ENV = "development"`
	* `flask run`
* CMD
	* `set FLASK_APP=flaskr`
	* `set FLASK_ENV=development`
	* `flask run`
* Bash
	* `export FLASK_APP=flaskr`
	* `export FLASK_ENV=development`
	* `flask run`

Link: https://theonlyweatherapp.herokuapp.com/
