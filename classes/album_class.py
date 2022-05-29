from flask_restful import  Resource, reqparse, abort, fields, marshal_with
from model import AlbumModel
from __init import db,app,request, jsonify

Album_put_args = reqparse.RequestParser()
Album_put_args.add_argument("name", type=str, help="Name of the Album is required", required=True)
Album_put_args.add_argument("singer", type=int, help="singer on the Album", required=True)



Album_update_args = reqparse.RequestParser()
Album_update_args.add_argument("name", type=str, help="Name of the Album is required")
Album_update_args.add_argument("singer", type=int, help="singer on the Album")

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
		if result:
			abort(409, message="Album id taken...")

		Album = AlbumModel(id=album_id, name=args['name'], singer=args['singer'])
		db.session.add(Album)
		db.session.commit()
		return Album, 201

	@marshal_with(resource_fields)
	def patch(self, album_id):
		args = Album_update_args.parse_args()
		result = AlbumModel.query.filter_by(id=album_id).first()
		if not result:
			abort(404, message="Album doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['singer']:
			result.singer = args['singer']

		db.session.commit()

		return result


	def delete(self, album_id):
		
		return '', 204

	@app.route("/postAlbum/", methods = ['POST'])
	def postNewAlbum():
		if request.method == 'POST':
			Album_put_args = reqparse.RequestParser()
			Album_put_args.add_argument("name", type=str, help="Name of the Album is required", required=True)
			Album_put_args.add_argument("singer", type=int, help="singer on the Album", required=True)
			args = Album_put_args.parse_args()
			print('aaaa:')
			Album = AlbumModel(name=args['name'],singer_id=args['singer'])
			db.session.add(Album)
			db.session.commit()
		return Album.to_json(), 201