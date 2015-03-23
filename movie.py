class Movie(object):
    
    """ A simpler movie Class """
    def __init__(self,mov_title,posterURL,youlink,runtime,genre,description,year,director):
        self.title = mov_title
        self.poster_image_url = posterURL
        self.trailer_youtube_url = youlink
        self.actors = []
        self.runtime = runtime
        self.genre = genre
        self.description = description
        self.year = year
        self.director = director
        self.tags = []
    
    def __init__(self, movie_params_list):
        self.title = movie_params_list[0]
        self.poster_image_url = movie_params_list[1]
        self.trailer_youtube_url = movie_params_list[2]
        self.runtime = movie_params_list[3]
        self.genre = movie_params_list[4]
        self.year = movie_params_list[5]
        self.director = movie_params_list[6]


    def add_actors(self,performers):
        self.actors = performers
    
    def add_movie_tags(self,indexs):
        self.tags = indexs


