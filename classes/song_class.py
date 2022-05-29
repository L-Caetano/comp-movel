from flask_restful import  Resource, reqparse, abort, fields, marshal_with
from model import SongModel
from __init import db,app,request, jsonify
from classes.album_class import Album
import json


song_put_args = reqparse.RequestParser()
song_put_args.add_argument("name", type=str, help="Name of the song is required", required=True)
song_put_args.add_argument("album", type=int, help="album of the song", required=True)


song_update_args = reqparse.RequestParser()
song_update_args.add_argument("name", type=str, help="Name of the song is required")
song_update_args.add_argument("album", type=int, help="album of the song")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'album': fields.Integer,
}
class Song(Resource):
	def get(self, song_id):
		result = SongModel.query.get(song_id)
		if not result:
			abort(404, message="Could not find song with that id")
		return jsonify(result.to_json())

	@marshal_with(resource_fields)
	def put(self, song_id):
		args = song_put_args.parse_args()
		result = SongModel.query.filter_by(id=song_id).first()
		if result:
			abort(409, message="song id taken...")
		song = SongModel(id=song_id, name=args['name'], album=args['album'], singer=args['album']['singer'])
		db.session.add(song)
		db.session.commit()
		return song, 201

	@marshal_with(resource_fields)
	def patch(self, song_id):
		args = song_update_args.parse_args()
		result = SongModel.query.filter_by(id=song_id).first()
		if not result:
			abort(404, message="song doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['album']:
			result.album = args['album']
		if args['singer']:
			result.singer = args['singer']

		db.session.commit()

		return result


	def delete(self, song_id):
		
		return '', 204
	
	@app.route("/postSong/", methods = ['POST'])
	def postNewSong():
		if request.method == 'POST':
			Song_put_args = reqparse.RequestParser()
			Song_put_args.add_argument("name", type=str, help="Name of the Song is required", required=True)
			Song_put_args.add_argument("album", type=int, help="Album of the Song is required", required=True)
			args = Song_put_args.parse_args()
			Song = SongModel(name=args['name'],album_id=args['album'])
			db.session.add(Song)
			db.session.commit()
		return Song.to_json(), 201
		#return str(args['album'])