from flask_restful import  Resource, reqparse, abort, fields, marshal_with
from model import SongModel
from __init import db

song_put_args = reqparse.RequestParser()
song_put_args.add_argument("name", type=str, help="Name of the song is required", required=True)
song_put_args.add_argument("album", type=int, help="album of the song", required=True)
song_put_args.add_argument("singer", type=int, help="singer on the song", required=True)

song_update_args = reqparse.RequestParser()
song_update_args.add_argument("name", type=str, help="Name of the song is required")
song_update_args.add_argument("album", type=int, help="album of the song")
song_update_args.add_argument("singer", type=int, help="singer on the song")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'album': fields.Integer,
	'singer': fields.Integer
}
class Song(Resource):
	@marshal_with(resource_fields)
	def get(self, song_id):
		result = SongModel.query.filter_by(id=song_id).first()
		if not result:
			abort(404, message="Could not find song with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, song_id):
		args = song_put_args.parse_args()
		result = SongModel.query.filter_by(id=song_id).first()
		if result:
			abort(409, message="song id taken...")

		song = SongModel(id=song_id, name=args['name'], album=args['album'], singer=args['singer'])
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