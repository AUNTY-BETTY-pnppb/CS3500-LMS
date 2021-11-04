class Book:

    def __init__(self, bookid, genre, name, author):
        # need to increment bookids automatically when creating books
        self._bookid = bookid
        self._genre = genre
        self._name = name
        self._author = author

    def __str__(self):
        return '%s %s' % (self._bookid, self._genre, self._name, self._author)

    def _set_bookid(self, bookid):
        # was talking to Odhran about any of the setters we might not need them
        # because ids,names etc.. should not change
        if type(bookid) != int:
            print("Invalid bookid")
        else:
            self._bookid = bookid

    def _set_genre(self, genre):
        if type(genre) != str:
            print("Invalid genre")
        else:
            self._genre = genre

    def _set_name(self, name):
        if type(name) != str:
            print("invalid name")
        else:
            self._name = name

    def _set_author(self, author):
        if type(author) != str:
            print("invalid author")
        else:
            self._author = author

    def _get_bookid(self):
        return self._bookid

    def _get_genre(self):
        return self._genre

    def _get_name(self):
        return self._name

    def _get_author(self):
        return self._author
