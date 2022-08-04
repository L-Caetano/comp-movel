from flask_restful import  Resource, reqparse, abort, fields, marshal_with
from model import SongModel, AlbumModel
from __init import db,app,request, jsonify
import json


song_put_args = reqparse.RequestParser()
song_put_args.add_argument("name", type=str, help="Nome da musica é required", required=True)
song_put_args.add_argument("album", type=int, help="Id do album é necessario", required=True)


song_update_args = reqparse.RequestParser()
song_update_args.add_argument("name", type=str, help="Nome da musica é required")
song_update_args.add_argument("album", type=int, help="Id do album é necessario")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'album': fields.Integer,
}
class Song(Resource):
	def get(self, song_id):
		result = SongModel.query.get(song_id)
		if not result:
			abort(404, message="Não foi possivel achar uma musica com esse id")
		return jsonify(result.to_json())

	@marshal_with(resource_fields)
	def put(self, song_id):
		args = song_put_args.parse_args()
		result = SongModel.query.filter_by(id=song_id).first()
		result.name=args['name'], 
		result.album=args['album']
		db.session.add(result)
		db.session.commit()
		return result, 201

	@marshal_with(resource_fields)
	def patch(self, song_id):
		args = song_update_args.parse_args()
		
		result = SongModel.query.filter_by(id=song_id).first()
		if not result:
			abort(404, message="Musica não existe não foi possivel ser mudada")
		
		if args['name']:
			result.name = args['name']
		if args['album']:
			result.album = AlbumModel.query.filter_by(id=args['album']).first()
		db.session.add(result)
		db.session.commit()

		return '', 201


	def delete(self, song_id):
		result = SongModel.query.filter_by(id=song_id).first() 
		if result:
			db.session.delete(result)
			db.session.commit()
		return '', 204
	
	@app.route("/postSong/", methods = ['POST'])
	def postNewSong():
		if request.method == 'POST':
			Song_put_args = reqparse.RequestParser()
			Song_put_args.add_argument("name", type=str, help="Nome da musica é required", required=True)
			Song_put_args.add_argument("album", type=int, help="Id do album é necessario", required=True)
			args = Song_put_args.parse_args()
			Song = SongModel(name=args['name'],album_id=args['album'])
			db.session.add(Song)
			db.session.commit()
		return Song.to_json(), 201
		#return str(args['album'])

	@app.route("/getAllSongs/", methods = ['GET'])
	def getAllSongs():
		if request.method == 'GET':
			p = SongModel.query.all()
			print(p)
			z = []
			for x in p:
				z.append(x.to_json())
			print(z)
		return json.dumps(z), 201
