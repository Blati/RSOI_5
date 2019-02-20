from services import root_dir, nice_json
from flask import Flask
from flask import request
from flask_cors import CORS
from werkzeug.exceptions import NotFound, ServiceUnavailable
import json
import requests
from logging import FileHandler, WARNING

app = Flask(__name__)

CORS(app)

with open("{}/database/users.json".format(root_dir()), "r") as f:
    users = json.load(f)
	
@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "users": "/users",
            "user": "/users/<username>",
			"auth": "/auth/login",
			"auth_reg": "/auth/register",
            "bookings": "/users/<username>/bookings",
            "bookings_add": "/users/<username>/bookings/add"
        }
    })

@app.route("/users", methods=['GET'])
def users_list():
    return nice_json(users)

@app.route("/auth/register", methods=['POST'])
def user_register():
    raw = json.dumps(request.get_json())
	
    try:
        result = requests.post("http://127.0.0.1:5004/register", raw)
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Authorization service is unavailable.")
	
    return nice_json(result.json())
	
@app.route("/auth/login", methods=['POST'])
def user_login():
    raw = json.dumps(request.get_json())

    try:
        result = requests.post("http://127.0.0.1:5004/login", raw)
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Authorization service is unavailable.")

    return nice_json(result.json())
	
@app.route("/users/<username>", methods=['GET'])
def user_record(username):
    if username not in users:
        raise NotFound

    return nice_json(users[username])

@app.route("/users/<username>/bookings", methods=['GET'])
def user_bookings(username):
    if username not in users:
        raise NotFound("User '{}' not found.".format(username))

    try:
        users_bookings = requests.get("http://127.0.0.1:5003/bookings/{}".format(username))
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable("The Bookings service is unavailable.")

    if users_bookings.status_code == 404:
        raise NotFound("No bookings were found for {}".format(username))

    users_bookings = users_bookings.json()

    # For each booking, get the rating and the movie title
    result = {}
    for date, movies in users_bookings.items():
        result[date] = []
        for movieid in movies:
            try:
                movies_resp = requests.get("http://127.0.0.1:5001/movies/{}".format(movieid))
            except requests.exceptions.ConnectionError:
                raise ServiceUnavailable("The Movie service is unavailable.")
            movies_resp = movies_resp.json()
            result[date].append({
                "title": movies_resp["title"],
                "rating": movies_resp["rating"],
                "uri": movies_resp["uri"]
            })

    return nice_json(result)

@app.route("/users/<username>/bookings/add", defaults={'page': '08022019'}, methods=['GET', 'POST'])
@app.route("/users/<username>/bookings/add/<page>", methods=['GET', 'POST'])
def user_bookings_add(username, page):

    if username not in users:
        raise NotFound("User '{}' not found.".format(username))

    if request.method == 'GET':
        result = {}
        try:
            showtimes = requests.get("http://127.0.0.1:5002/showtimes/{}".format(page))
        except requests.exceptions.ConnectionError:
            raise ServiceUnavailable("The Showtimes service is unavailable.")
		
        showtimes = showtimes.json()
       
        for movieid in showtimes:
            result[movieid] = []
            try:
                movies_resp = requests.get("http://127.0.0.1:5001/movies/{}".format(movieid))
            except requests.exceptions.ConnectionError:
                raise ServiceUnavailable("The Movie service is unavailable.")
            try:
                movies_resp = movies_resp.json()
            except ValueError:
                raise ServiceUnavailable("Sorry! No movies in this day.")
            result[movieid].append({
                "title": movies_resp["title"],
                "rating": movies_resp["rating"]
            })
			
        return nice_json(result)

    if request.method == 'POST':
        raw = request.get_json()
        result = requests.post("http://127.0.0.1:5003/bookings/{}/add".format(username), json={username:raw})
        result = result.json()
		
        user_resp = requests.get("http://127.0.0.1:5000/users/{}".format(username))
        user_resp = user_resp.json()
        content = {
            "id": user_resp["id"],
            "name": user_resp["name"],
            "last_active": 0
        }
        content = {username:content}
        with open("{}/database/users.json".format(root_dir())) as ff:
            data = json.load(ff)        
		
        data.update(content)
        with open("{}/database/users.json".format(root_dir()), "w+") as ff:
            json.dump(data,ff)
        users.update(content)	
        return nice_json(result)

    raise NotImplementedError()				


if __name__ == "__main__":
    app.run(port = 5000, debug = True)