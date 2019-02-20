from services import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json
from logging import FileHandler, WARNING

app = Flask(__name__)

file_handler = FileHandler('logs/movies_log.log')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

with open("{}/database/movies.json".format(root_dir()), "r") as f:
    movies = json.load(f)

@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>"
        }
    })

@app.route("/movies/<movieid>", methods=['GET'])
def movie_info(movieid):
    if movieid not in movies:
        raise NotFound

    result = movies[movieid]
    result["uri"] = "/movies/{}".format(movieid)

    return nice_json(result)

@app.route("/movies", methods=['GET'])
def movie_record():
    return nice_json(movies)


if __name__ == "__main__":
    app.run(port=5001, debug = True)