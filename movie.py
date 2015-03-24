class Movie(object):
    ''' The class Movie represents and object called Movie.
    As it is expected, it has fields such as title, poster and trailer URL.
    In order to go a little further, I add the fields runtime, the duration of the movie
    its genre, the year it was presented, the director and for further information, a link to the imdb website
    for the movie
    '''
    # Defined a constructor for a Movie Object, where the attributes of the object are taken from a List called movie_params_list.
    def __init__(self, movie_params_list):
        self.title = movie_params_list[0]
        self.poster_image_url = movie_params_list[1]
        self.trailer_youtube_url = movie_params_list[2]
        self.runtime = movie_params_list[3]
        self.genre = movie_params_list[4]
        self.year = movie_params_list[5]
        self.director = movie_params_list[6]
        self.imdb_information = movie_params_list[7]


