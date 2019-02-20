from services import root_dir, nice_json
from flask import Flask, jsonify, request, json
from flask_pymongo  import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'authusers'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/authusers'
app.config['JWT_SECRET_KEY'] = 'definetly_not_a_secret_key'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

@app.route("/register", methods=['POST'])
def user_register():
    auth = mongo.db.auth
    first_name = request.get_json(force=True)['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()

    user_id = auth.insert({
	'first_name' : first_name, 
	'last_name' : last_name, 
	'email' : email, 
	'password' : password, 
	'created' : created, 
	})
    new_user = auth.find_one({'_id' : user_id})

    result = {'result' : {'email' : new_user['email'] + ' registered'}}

    return nice_json(result)
	
@app.route("/login", methods=['POST'])
def user_login():
    auth = mongo.db.auth
    email = request.get_json(force=True)['email']
    password = request.get_json()['password']
    result = ""
	
    response = auth.find_one({'email' : email})

    if response:	
        if bcrypt.check_password_hash(response['password'], password):
            access_token = create_access_token(identity = {
			    'first_name': response['first_name'],
				'last_name': response['last_name'],
				'email': response['email']}
				)
            result = nice_json({"token":access_token})
        else:
            result = nice_json({"error":"Invalid username and password"})            
    else:
        result = nice_json({"result":"No results found"})

    return result
	
	
if __name__ == "__main__":
    app.run(port = 5004, debug = True)