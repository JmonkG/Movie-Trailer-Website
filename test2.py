from movie import Movie
from fresh_tomatoes import *
list_movies = []
movie_file = open("movies.txt","r")

for line in movie_file:
    list_movies.append(Movie(line.split(',')))
    
open_movies_page(list_movies)
