from movie import Movie
import fresh_tomatoes

m = Movie('Prueba','http:','http2:',20,'Comedy','fun',1994,'me')
m.add_actors(['melina','mariloli','josue','diana','walter'])
m.add_movie_tags(['Quevedo','Ciudad del Rio','Gye'])

print m.title,m.actors,m.tags
