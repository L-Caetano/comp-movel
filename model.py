from __init import db

class SingerModel(db.Model):
	__tablename__ = "singer"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	
	def __repr__(self):
		return f"album(name =, singer = )"


class AlbumModel(db.Model):
	__tablename__ = "album"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	singer_id = db.Column(db.Integer, db.ForeignKey("singer.id"))
	singer = db.relationship("SingerModel")
	
	def __repr__(self):
		return f""

class SongModel(db.Model):
	__tablename__ = "song"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	singer_id = db.Column(db.Integer, db.ForeignKey("singer.id"))
	singer = db.relationship("SingerModel")
	album_id =  db.Column(db.Integer, db.ForeignKey("album.id"))
	album = db.relationship("AlbumModel")
	def __repr__(self):
		return f""


