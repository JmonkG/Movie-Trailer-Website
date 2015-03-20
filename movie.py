class Movie(object):
    
    """ A simpler movie Class """
    def __init__(self,mov_title,posterURL,youlink,runtime,genre,description,year,director):
        self.title = mov_title
        self.posURL = posterURL
        self.ylink = youlink
        self.actors = []
        self.runtime = runtime
        self.genre = genre
        self.description = description
        self.year = year
        self.director = director
        self.tags = []
    
    def add_actors(self,performers):
        self.actors = performers
    
    def add_movie_tags(self,indexs):
        self.tags = indexs


