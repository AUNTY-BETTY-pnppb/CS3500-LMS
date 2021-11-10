from Bookshelf import *

class Book:

    def __init__(self, genre, name, author):
        # need to increment bookids automatically when creating books
        self._genre = genre
        self._name = name
        self._author = author
        self._availability = True
        self._bookid = id(self)

    def __str__(self):
        return 'Title: %s  | Author: %s  | Genre: %s  ' % (self._name, self._author, self._genre)

    def _getBookId(self):
        return self._bookid

    def _getGenre(self):
        return self._genre

    def _getName(self):
        return self._name

    def _getAuthor(self):
        return self._author

    def isAvailable(self):
        if self._availability == True:
            return "Available"
        else:
            return "Unavailable"

    def _getAvailability(self):
        return self._availability

    def _setAvailability(self, availability):
        self._availability = availability
