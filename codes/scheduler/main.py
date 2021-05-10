from plexapi.server import PlexServer

baseurl = 'http://jbchhn.synology.me:32500'
token = '8fB6XveqmX6UN1Lrd8Rz'
plex = PlexServer(baseurl, token)

movies = plex.library.sections()
print(movies)
for i in movies[0].search():
    print(i)

print(plex.sessions())

