from flask_restful import  Resource, reqparse, abort, fields, marshal_with
from model import SingerModel
from model import AlbumModel
from flask import jsonify
from sqlalchemy.orm import sessionmaker
from __init import db, request, app
import json

Singer_put_args = reqparse.RequestParser()
Singer_put_args.add_argument("name", type=str, help="Nome do artista é necessario", required=True)

Singer_update_args = reqparse.RequestParser()
Singer_update_args.add_argument("name", type=str, help="Nome do artista é necessario")


resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
}
class Singer(Resource):
	@marshal_with(resource_fields)
	def get(self, singer_id):
		result = SingerModel.query.filter_by(id=singer_id).first()
		if not result:
			abort(404, message="Não foi possivel encotrar uma musica com esse id")
		return result

	@marshal_with(resource_fields)
	def post(self, singer_id):
		args = Singer_put_args.parse_args()
	#	result = SingerModel.query.filter_by(id=singer_id).first()
	#	if result:
	#		abort(409, message="Singer id taken...")

		Singer = SingerModel(name=args['name'])
		db.session.add(Singer)
		db.session.commit()
		return Singer, 201

	@marshal_with(resource_fields)
	def put(self, singer_id):
		args = Singer_update_args.parse_args()
		result = SingerModel.query.filter_by(id=singer_id).first()
		if not result:
			abort(404, message="Cantor não existe, não foi possivel mudar")

		if args['name']:
			result.name = args['name']
		if args['album']:
			result.album = args['album']
		if args['songs']:
			result.songs = args['songs']

		db.session.commit()

		return result


	def delete(self, singer_id):
		result = SingerModel.query.filter_by(id=singer_id).first() 
		if result:
			db.session.delete(result)
			db.session.commit()
		return '', 204
	
	@marshal_with(resource_fields)
	def patch(self, singer_id):
		args = Singer_put_args.parse_args()
		result = SingerModel.query.filter_by(id=singer_id).first()
		if not result:
			abort(404, message="Musica não existe não foi possivel ser mudada")	
		if args['name']:
			result.name = args['name']
	
		db.session.add(result)
		db.session.commit()

		return '', 201
	
	@app.route("/postSinger/", methods = ['POST'])
	def postNewSinger():
		if request.method == 'POST':
			Singer_put_args = reqparse.RequestParser()
			Singer_put_args.add_argument("name", type=str, help="Nome do artista é necessario", required=True)
			args = Singer_put_args.parse_args()
			Singer = SingerModel(name=args['name'])
			db.session.add(Singer)
			db.session.commit()
		return str(Singer), 201


	@app.route("/getAllSingers/", methods = ['GET'])
	def getAllSingers():
			if request.method == 'GET':
				p = SingerModel.query.all()
				print(p)
				z = []
				for x in p:
					z.append(x.to_json())
			print(z)

			
			return json.dumps(z), 201
