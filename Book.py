from Bookshelf import *
import random

class Book:

    def __init__(self, genre, name, author, availability=True):
        # need to increment bookids automatically when creating books
        self._genre = genre
        self._name = name
        self._author = author
        self._availability = availability
        self._bookid = random.randint(1000000000000, 9999999999999)

    def __str__(self):
        # i have changed the strings around to make it look less chaotic
        genreList =  {"Action": "Action    ", "Romance": "Romance", "Fantasy": "Fantasy   ", "Sci-fi": "Sci-fi       ", "Drama": "Drama    ", "Horror": "Horror    "}
        return 'ID: %s  Avail: %s       %s      %s, by %s' % (str(self._bookid), self.isAvailable(), genreList[self.getGenre()], self._name, self._author)

    def _getBookId(self):
        return self._bookid

    def getGenre(self):
        return self._genre

    def getName(self):
        return self._name

    def getAuthor(self):
        return self._author

    def isAvailable(self):
        if self._availability:
            return "O"
        else:
            return "X"

    def _getAvailability(self):
        return self._availability

    def _setAvailability(self, availability):
        self._availability = availability
