from movie import Movie
import fresh_tomatoes

m = []
m.append(Movie("Shidler's List",'http://goo.gl/D9A7ak','https://www.youtube.com/watch?v=JdRGC-w9syA',20,'Comedy','fun',1994,'me'))
m.append(Movie('The Matrix','http://goo.gl/oZNWwv','https://www.youtube.com/watch?v=JdRGC-w9syA,20','Comedy','fun',1994,'me'))
m.append(Movie('Avengers','http://goo.gl/DuPSZI','http://goo.gl/r9lAzm',20,'Comedy','fun',1994,'me'))
m.append(Movie('UP','http://goo.gl/zcZHiL','http://goo.gl/Vq8IBQ',20,'Comedy','fun',1994,'me'))
m.append(Movie('American Sniper','http://goo.gl/i9CBY8','http://goo.gl/WSBLdc',20,'Comedy','fun',1994,'me'))

open_movies_page(m)
