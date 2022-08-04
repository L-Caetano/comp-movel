from __init import db

class SingerModel(db.Model):
	__tablename__ = "singer"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	song = db.relationship("AlbumModel", back_populates="singer", cascade="all, delete-orphan")
	def to_json(self):
		return {
			'id': self.id,
			'name': self.name,
		}


class AlbumModel(db.Model):
	__tablename__ = "album"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	singer_id = db.Column(db.Integer, db.ForeignKey("singer.id"))
	singer = db.relationship("SingerModel")
	song = db.relationship("SongModel", back_populates="album", cascade="all, delete-orphan")
	def to_json(self):
		return {
			'id': self.id,
			'name': self.name,
			'singer': self.singer.to_json()
		}

class SongModel(db.Model):
	__tablename__ = "song"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	album_id =  db.Column(db.Integer, db.ForeignKey("album.id"))
	album = db.relationship("AlbumModel")
	
	def to_json(self):
		return {
			'id': self.id,
			'name': self.name,
			'album': self.album.to_json()
		}

	


