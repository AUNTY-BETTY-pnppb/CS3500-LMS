from Bookshelf import *

class Book:

    def __init__(self, genre, name, author):
        # need to increment bookids automatically when creating books
        self._genre = genre
        self._name = name
        self._author = author
        self._availability = True
        self._bookid = id()

    def __str__(self):
        return '%s %s %s %s' % (self._bookid, self._genre, self._name, self._author)

    def _getBookId(self):
        return self._bookid

    def _getGenre(self):
        return self._genre

    def _getName(self):
        return self._name

    def _getAuthor(self):
        return self._author

    def isAvailable(self):
        return self._availability

    def _setAvailability(self, availability):
        self._availability = availability
