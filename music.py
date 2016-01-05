class Artist:
	def __init__(self, name):
		self.name = name

		self.albums = []
		self.songs = []

	def __repr__(self):
		return '<Artist: %s>' % self.name

	def add_album(self, album):
		self.albums.append(album)

	def add_song(self, song):
		self.songs.append(song)	


class Album:
	def __init__(self, title, year, artist_list=[]):
		self.title = title
		self.year = year

		self.songs = []
		self.artists = []

		if len(artist_list) > 0:
			[(self.artists.append(artist), artist.add_album(self))\
			 for artist in artist_list]

	def __repr__(self):
		return '<Album: %s>' % self.title

	def add_song(self, song):
		self.songs.append(song)

	def add_artist(self, artist):
		self.artists.append(artist)
		artist.add_album(self)

	def song_count(self):
		return len(self.songs)

	def album_artists(self):
		return ', '.join(artist.name for artist in self.artists)


class Song:
	def __init__(self, title, length, album_list=[], artist_list=[]):
		self.title = title
		self.length = length

		self.albums = []
		self.artists = []

		if len(artist_list) > 0:
			[(self.artists.append(artist), artist.add_song(self))\
			 for artist in artist_list]

		if len(album_list) > 0:
			[(self.albums.append(album), album.add_song(self))\
			 for album in album_list]

	def __repr__(self):
		return '<Song: %s>' % self.title

	def add_album(self, album):
		self.albums.append(album)
		album.add_song(self)

	def add_artist(self, artist):
		self.artists.append(artist)
		artist.songs.append(self)


class Playlist:
	def __init__(self, name):
		self.name = name
		self.songs = {}

	def __repr__(self):
		return '<Playlist: %s>' % self.name

	def add_song(self, song):
		self.songs[song.title] = song
		return '{} added to playlist'.format(song.title)

	def remove_song(self, song):
		del self.songs[song.title]
		return '{} removed to playlist'.format(song.title)

	def list_tracks(self):
		print 'Track Title\tArtist(s)\tAlbum(s)'
		print '=' * 40
		for k, v in self.songs.iteritems():
			print (v.title + '\t' + 
				   ', '.join(artist.name for artist in v.artists) + '\t' +
				   ', '.join(album.title for album in v.albums)
				   )


artist1=Artist(name='Artist 1')
artist2=Artist(name='Artist 2')
artist3=Artist(name='Artist 3')

album1=Album(title='Album One', year=2010, artist_list=[artist1])
album2=Album(title='Album Two', year=2000, artist_list=[artist2])
album3=Album(title='Album Three - Compilation', year=1990, 
	artist_list=[artist1, artist2, artist3])

song1=Song(title='Song One', length='2:30', album_list=[album1, album3], 
	artist_list=[artist1, artist2])
song2=Song(title='Song Two', length='3:30', album_list=[album2, album3], 
	artist_list=[artist2])
song3=Song(title='Song Three', length='2:50', album_list=[album3], 
	artist_list=[artist3])
song4=Song(title='Song Four', length='4:10', album_list=[album1], 
	artist_list=[artist3])
song5=Song(title='Song Five', length='3:50', album_list=[album2], 
	artist_list=[artist3])

playlist1=Playlist(name='Cool Songs')
playlist2=Playlist(name='Even Cooler Songs')

playlist1.add_song(song1)
playlist1.add_song(song3)
playlist1.add_song(song4)
playlist1.add_song(song5)
playlist1.remove_song(song5)

playlist2.add_song(song2)
playlist2.add_song(song4)
playlist2.add_song(song5)