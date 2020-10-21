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
    
    # data_json = jsonify(data)
    
    # errors = validate_data(data_json)
    errors = validate_data(data)

    if errors['errors']:
        # return jsonify({errors})
        return errors

    res = get_trivia(data['year'])

    return res


def request_year_trivia(year):
    """Return year and fact from Numbers API for given year."""

    res = requests.get(f'{API_BASE_URL}/{year}/year?json')

    # data = {params: {"number": year, "type": "year"}}

    # where does ? json go?
    # headers = {["Content-Type"]: "application/json"}
    # res = requests.get(f'{API_BASE_URL}/{year}/year', headers=headers)
    
    return res


def request_num_trivia():
    """Return number and trivia from Numbers API for random number."""

    res = requests.get(f'{API_BASE_URL}/random?min=1&max=100&json')

    return res

def get_trivia(year):
    """Get trivia based on form input.
    Will run only if there are no errors in data from client."""

    # *************************************************
    # make API request to Numbers API using those data
    # *************************************************
    res_num_trivia = request_num_trivia()
    data_num=res_num_trivia.json()
    num_info = {"fact": data_num['text'], "num": data_num['number']}

    # with specific year: res_year_trivia = request_year_trivia(1969)
    res_year_trivia = request_year_trivia(year)
    data_year=res_year_trivia.json()
    year_info = {"fact": data_year['text'], "year": data_year['number']}

    res_json = {"num": num_info, "year": year_info}
    return res_json


def get_form_data():
    """Get data from client form."""

    # GET FORM INPUT DATA from lucky.js

    data = {}
    data['name'] = request.json['name']
    data["year"] = request.json['year']
    data["email"] = request.json['email']
    data["color"] = request.json['color']

    return data

# check data for errors
def validate_data(data):
    """Check data from client for errors."""
    valid_colors = ["red", "green", "orange", "blue"]
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
    if (not data["color"]) or (data["color"] not in valid_colors):
        color_err = ["Invalid value, must be one of: red, green, orange, blue."]
        errors['errors']['color'] = color_err

    return errors

    # send get request to Numbers API and receive response

    # res_json = get_trivia()

    # send the response
    # return res_json








# ***************************************************************
# *******************
# ATTEMPTS TO CALL API
# *******************
    # res = requests.get(f'{API_BASE_URL}/random?min=1&max=100?json')
    # res = requests.get(f'{API_BASE_URL}/random?min=1&max=100/trivia?json')
    # res = requests.get(f'{API_BASE_URL}/random?min=1&max=100/trivia?json')


# *******************


    # data[text]
    # data.get[number]
    # return data
    # res_json = jsonify(data=data)



    # res2 = requests.get(f'{API_BASE_URL}/1969/year?json')

    # res = requests.get(f'{API_BASE_URL}', params={'number': 'random', 'type': 'trivia'});
    # url = f"{API_BASE_URL}"

    # res = requests.get(url, params={'number': 'random', 'type': 'trivia'}, headers={'Content-Type': 'application/json'})
    # res = jsonify(requests.get(url, params={'number': 'random', 'type': 'trivia'}))
    # res = requests.get(url, params={'number': 'random', 'type': 'trivia'}).headers["Content-Type"] = "application/json"
    # res.headers["Content-Type"] = "application/json"
    # data=res.json()
    # res_json = jsonify(data=data)
    # res1 = requests.get(f'{API_BASE_URL}/random/trivia?json')
    # res2 = requests.get(f'{API_BASE_URL}/1969/year?json')
