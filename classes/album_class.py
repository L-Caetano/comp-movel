from flask_restful import  Resource, reqparse, abort, fields, marshal_with
from model import AlbumModel
from __init import db

Album_put_args = reqparse.RequestParser()
Album_put_args.add_argument("name", type=str, help="Name of the Album is required", required=True)
Album_put_args.add_argument("song", type=int, help="song of the song", required=True)
Album_put_args.add_argument("singer", type=int, help="singer on the Album", required=True)

Album_update_args = reqparse.RequestParser()
Album_update_args.add_argument("name", type=str, help="Name of the Album is required")
Album_update_args.add_argument("song", type=int, help="song of the song")
Album_update_args.add_argument("singer", type=int, help="singer on the Album")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'song': fields.Integer,
	'singer': fields.Integer
}
class Album(Resource):
	@marshal_with(resource_fields)
	def get(self, Album_id):
		result = AlbumModel.query.filter_by(id=Album_id).first()
		if not result:
			abort(404, message="Could not find Album with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, Album_id):
		args = Album_put_args.parse_args()
		result = AlbumModel.query.filter_by(id=Album_id).first()
		if result:
			abort(409, message="Album id taken...")

		Album = AlbumModel(id=Album_id, name=args['name'], song=args['song'], singer=args['singer'])
		db.session.add(Album)
		db.session.commit()
		return Album, 201

	@marshal_with(resource_fields)
	def patch(self, Album_id):
		args = Album_update_args.parse_args()
		result = AlbumModel.query.filter_by(id=Album_id).first()
		if not result:
			abort(404, message="Album doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['song']:
			result.song = args['song']
		if args['singer']:
			result.singer = args['singer']

		db.session.commit()

		return result


	def delete(self, Album_id):
		
		return '', 204