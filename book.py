class Book:

    def __init__(self, bookid, genre, name, author):
        # need to increment bookids automatically when creating books
        self._bookid = bookid
        self._genre = genre
        self._name = name
        self._author = author
        self._availability = True

    def __str__(self):
        return '%s %s' % (self._bookid, self._genre, self._name, self._author)

    def _setBookId(self, bookid):
        # was talking to Odhran about any of the setters we might not need them
        # because ids,names etc.. should not change
        if type(bookid) != int:
            print("Invalid bookid")
        else:
            self._bookid = bookid

    def _setGenre(self, genre):
        if type(genre) != str:
            print("Invalid genre")
        else:
            self._genre = genre

    def _setName(self, name):
        if type(name) != str:
            print("invalid name")
        else:
            self._name = name

    def _setAuthor(self, author):
        if type(author) != str:
            print("invalid author")
        else:
            self._author = author


    def _getBookId(self):
        return self._bookid

    def _getGenre(self):
        return self._genre

    def _getName(self):
        return self._name

    def _getAuthor(self):
        return self._author
