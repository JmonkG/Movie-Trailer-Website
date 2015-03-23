'''
This is the main file, where a list of movies is created. Every movie is storage on a local file movies.txt
This program reads every line of the file, wich corresponds to a movie and with the split() function it
transform to a list of strings. This list is passed to the constructor of the Movie and then append to the movie_List.
After having the list of movies ready, it is passed to the open_movies_page function from fresh tomatoes.py
'''
from movie import Movie
from fresh_tomatoes import *
movies_list = [] #list of movies

movie_file = open("movies.txt","r") #file containing the parameters of the movies. Open in read mode

for line in movie_file:
    movies_list.append(Movie(line.split(','))) # For every line on the file, apply the split function and pass it to the Movie constructor
    
open_movies_page(movies_list) # send the list of movies to the movies page
