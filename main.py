from model import SongModel
from flask_restful import  Resource, reqparse, abort, fields, marshal_with
from __init import db,app,api, request
from classes.song_class import Song
from classes.album_class import Album 
from classes.singer_class import Singer
from model import SingerModel


db.create_all();


api.add_resource(Song, "/song/<int:song_id>")
api.add_resource(Singer, "/singer/<int:singer_id>")
api.add_resource(Album, "/album/<int:album_id>")

if __name__ == "__main__":
	app.run(debug=True)