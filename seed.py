from models import Playlist, Song, PlaylistSong, db
from app import app


db.drop_all()
db.create_all()

# Create dummy song
song1 = Song(title="Pare Ko", artist="Eraserheads")
song2 = Song(title="Gitara", artist="Parokya Ni Edgar")
song3 = Song(title="Pare", artist="Jay Pegarido")

db.session.add(song1)
db.session.add(song2)
db.session.add(song3)

db.session.commit()

# create dummy playlist
pl1 = Playlist(name="Personal", description="Songs written by me")
pl2 = Playlist(name="OPM", description="Original Pinoy Music")

db.session.add(pl1)
db.session.add(pl2)

db.session.commit()


# Create Playlistsong table
pls1 = PlaylistSong(playlist_id=1, song_id=3)
pls2 = PlaylistSong(playlist_id=2, song_id=1)
pls3 = PlaylistSong(playlist_id=2, song_id=2)

db.session.add(pls1)
db.session.add(pls2)
db.session.add(pls3)

db.session.commit()
