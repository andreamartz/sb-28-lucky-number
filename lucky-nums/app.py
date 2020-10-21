from flask import Flask, request, render_template
import requests
from flask_debugtoolbar import DebugToolbarExtension


API_BASE_URL = 'http://numbersapi.com'


app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors by showing custom 404 page."""

    return render_template('404.html'), 404


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route('/api/get-lucky-num', methods=["POST"])
def get_lucky_num():
    """Get trivia based on form input."""

    data = get_form_data()
    
    errors = validate_data(data)

    if errors['errors']:
        return errors

    res = get_trivia(data['year'])

    return (res, 201)


def request_year_trivia(year):
    """Return year and fact from Numbers API for given year."""

    res = requests.get(f'{API_BASE_URL}/{year}/year?json')
   
    return res


def request_num_trivia():
    """Return number and trivia from Numbers API for random number."""

    MIN_NUM = 1
    MAX_NUM = 100

    res = requests.get(f'{API_BASE_URL}/random?min={MIN_NUM}&max={MAX_NUM}&json')

    return res


def get_trivia(year):
    """Get trivia based on form input."""

    # make API requests to Numbers API using data from client

    res_num_trivia = request_num_trivia()
    num_trivia_json=res_num_trivia.json()
    num_info = {"fact": num_trivia_json['text'], "num": num_trivia_json['number']}

    # with specific year: res_year_trivia = request_year_trivia(1969)
    res_year_trivia = request_year_trivia(year)
    year_trivia_json=res_year_trivia.json()
    year_info = {"fact": year_trivia_json['text'], "year": year_trivia_json['number']}

    res = {"num": num_info, "year": year_info}
    return res


def get_form_data():
    """Get data from client form."""

    # get form input data from lucky.js
    data = {}
    data['name'] = request.json['name']
    data["year"] = request.json['year']
    data["email"] = request.json['email']
    data["color"] = request.json['color']

    return data


def validate_data(data):
    """Check data from client for errors."""

    VALID_COLORS = ["red", "green", "orange", "blue"]

    # set error text (if error exists) for each form field
    errors = {'errors': {}}

    if not data["name"]:
        name_err = ["This field is required."]
        errors['errors']['name'] = name_err

    if (not data["year"]) or (int(data["year"]) < 1900) or (int(data["year"]) > 2000):
        year_err = ["Invalid value, must be between 1900 and 2000."]
        errors['errors']['year'] = year_err

    if not data["email"]:
        email_err = ["This field is required."]
        errors['errors']['email'] = email_err

    if (not data["color"]) or (data["color"] not in VALID_COLORS):
        color_err = ["Invalid value, must be one of: red, green, orange, blue."]
        errors['errors']['color'] = color_err

    return errors

