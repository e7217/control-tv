from plexapi.server import PlexServer
import env

baseurl = env.URL
token = env.TOKEN
plex = PlexServer(baseurl, token)

movies = plex.library.sections()
print(movies)
for i in movies[0].search():
    print(i)
print(plex.systemDevice(4))
print(plex.sessions())

