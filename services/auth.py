from services import root_dir, nice_json
from flask import Flask, jsonify, request, json
from flask_pymongo  import PyMongo
from bson.objectid import ObjectId
import datetime
import json
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, fresh_jwt_required
)

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
    created = datetime.datetime.utcnow()

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
            ret = {
                'access_token' : create_access_token(identity = {
			        'first_name': response['first_name'],
				    'last_name': response['last_name'],
				    'email': response['email']}, expires_delta=datetime.timedelta(minutes=30)),
                'refresh_token' : create_refresh_token(identity = {
			        'first_name': response['first_name'],
				    'last_name': response['last_name'],
				    'email': response['email']})	
            }				
            result = nice_json(ret)
            with open("{}/tokens/token.json".format(root_dir()), "w") as f:
                json.dump(ret,f)
        else:
            result = nice_json({"error":"Invalid username and password"})            
    else:
        result = nice_json({"result":"No results found"})

    return result, 200

@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user)
    }
    with open("{}/tokens/token.json".format(root_dir()), "w") as f:
        json.dump(ret,f)
    return nice_json(ret)	

@app.route('/check', methods=['GET'])
@jwt_required
def check():
    ret = {'msg':'OK'}
    result = nice_json(ret)
    return result, 200



if __name__ == "__main__":
    app.run(port = 5004, debug = True)