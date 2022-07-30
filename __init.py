from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request,jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_cors import CORS 
app = Flask(__name__)
api = Api(app)
CORS(app)
cors = CORS(app, resources={
	r"/*": {
		"origins": "*"
		}
		})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
