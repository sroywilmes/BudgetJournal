

class Movie():


    def __init__(self, title, director, index):
        self.title = title
        self.director = director
        self.watched = False
        self.index = index
        self.rating = "0"

    def setRating(self, rating):
        self.rating = rating
        self.watched = True



class Database():

    watchedMovieCount = 0
    totalMovieCount = 0
    movies = []

    def __init__(self, movies):
        self.movies = movies
        for i in range(len(movies)):
            if movies[i].rating != "0":
                self.watchedMovieCount += 1
            self.totalMovieCount += 1

    def addMovie(self, title, director, rating):
        new_movie = Movie(title, director, self.totalMovieCount)

        if rating != '0':
            new_movie.setRating(rating)
            self.watchedMovieCount += 1

        print(self.totalMovieCount)
        self.movies.append(new_movie)
        self.totalMovieCount += 1

    def rateMovie(self):
        for i in range(self.totalMovieCount):
            if self.movies[i].rating == "0":
                print('#{i} : {t}'.format(i=i, t = self.movies[i].title))

        choice = int(input("Enter the index of the movie you wish you rate: "))

        self.movies[choice].setRating(input("Enter your rating for {i}: ".format(i=self.movies[choice].title)))
        self.watchedMovieCount += 1

    def listMovies(self):
        print("\n\n\nTotal Movies: " + str(self.totalMovieCount))
        print("Watched Movies: " + str(self.watchedMovieCount) + '\n')
        print('{:20}'.format("Title:") + '{:20}'.format("Director:") + '{:20}'.format("Rating: "))
        print('{:20}'.format("------") + '{:20}'.format("---------") + '{:20}'.format("------- "))
        for i in range(self.totalMovieCount):
            titleString= self.movies[i].title
            '{:20}'.format(titleString)

            directorString = self.movies[i].director
            '{:20}'.format(directorString)

            ratingString = self.movies[i].rating
            '{:20}'.format(ratingString)
            movieString = titleString + directorString + ratingString
            print('{:20}'.format(titleString) +'{:20}'.format(directorString)+'{:20}'.format(ratingString))
        print('\n\n')
    def listWantedMovies(self):
        print("\n\nHere are some movies you've added but haven't watched yet\n")
        print('{:20}'.format("Title:") + '{:20}'.format("Director:"))
        print('{:20}'.format("------") + '{:20}'.format("---------"))
        for i in range(self.totalMovieCount):
            if str(self.movies[i].rating) == "0":
                titleString = self.movies[i].title
                '{:20}'.format(titleString)

                directorString = self.movies[i].director
                '{:20}'.format(directorString)


                movieString = titleString + directorString
                print('{:20}'.format(titleString) + '{:20}'.format(directorString))
        print("\n\n")




