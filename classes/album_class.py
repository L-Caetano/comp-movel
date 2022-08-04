from flask_restful import  Resource, reqparse, abort, fields, marshal_with
from model import AlbumModel
from model import SongModel
from model import SingerModel

from classes.song_class import Song

from __init import db,app,request, jsonify
import json

Album_put_args = reqparse.RequestParser()
Album_put_args.add_argument("name", type=str, help="Nome do album é necessario", required=True)
Album_put_args.add_argument("singer", type=int, help="Singer é necessario", required=True)



Album_update_args = reqparse.RequestParser()
Album_update_args.add_argument("name", type=str, help="Nome do album é necessario")
Album_update_args.add_argument("singer", type=int, help="Singer é necessario")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'singer': fields.Integer
}


class Album(Resource):
	
	def get(self, album_id):
		result = AlbumModel.query.get(album_id)
		if not result:
			abort(404, message="Could not find Album with that id")
		return jsonify(result.to_json())

	@marshal_with(resource_fields)
	def put(self, album_id):
		args = Album_put_args.parse_args()
		result = AlbumModel.query.filter_by(id=album_id).first()
		
		result.name=args['name'], 
		result.singer=args['singer']
		db.session.add(result)
		db.session.commit()
		return result, 201

	@marshal_with(resource_fields)
	def patch(self, album_id):
		args = Album_update_args.parse_args()
		result = AlbumModel.query.filter_by(id=album_id).first()
		if not result:
			abort(404, message="Album doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['singer']:
			result.singer = SingerModel.query.filter_by(id=args['singer']).first()

		db.session.add(result)
		db.session.commit()

		return '', 201


	def delete(self, album_id):
		result = AlbumModel.query.filter_by(id=album_id).first() 
		if result:
			db.session.delete(result)
			db.session.commit()
		return '', 204

	@app.route("/postAlbum/", methods = ['POST'])
	def postNewAlbum():
		if request.method == 'POST':
			Album_put_args = reqparse.RequestParser()
			Album_put_args.add_argument("name", type=str, help="Nome do album é necessario", required=True)
			Album_put_args.add_argument("singer", type=int, help="Singer é necessario", required=True)
			args = Album_put_args.parse_args()
			print('aaaa:')
			Album = AlbumModel(name=args['name'],singer_id=args['singer'])
			db.session.add(Album)
			db.session.commit()
		return Album.to_json(), 201

	@app.route("/getAlbumBySinger/", methods = ['GET'])
	def getAlbumBySinger():
		if request.method == 'GET':
			singer_id = request.args.get('singer_id')		
			z = []
			for p in AlbumModel.query.filter_by(singer_id = singer_id):
				z.append(p.to_json())
			print(p)
			
		return json.dumps(z), 201

	@app.route("/getAllAlbum/", methods = ['GET'])
	def getAllAlbum():
		if request.method == 'GET':
			p = AlbumModel.query.all()
			
		
			z = []
			#y = []
		
			for x in p:
				px = []
				for xu in SongModel.query.filter_by(album_id = x.id):	
					
					px.append(xu.to_json())
				y = {"album": x.to_json(),"songs": px}
				z.append(y)

			
		return json.dumps(z), 201