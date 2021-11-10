from Book import *
from datetime import datetime, timedelta

class User:

    def __init__(self, username, email, password):
        #will need a check to shelf to see if an existing user
        #or email exists when creating a new user
        self._username = username
        self._email = email
        self._password = password
        self.borrowlist = {}
        self.reservelist = []

    def __str__(self):
        return '%s %s' % (self._username, self._email)

    def _setUsername(self, username):
        #check shelf again for existing
        if type(username) != str:
            print("Invalid username")
        else:
            self._username = username

    def _setEmail(self, email):
        #check shelf again for existing
        if type(email) != str:
            print("Invalid email")
        else:
            self._email = email

    def _setPassword(self, password):
        # some check if we want to have a password eg. 8chars long etc...
        if type(password) != str:
            print("invalid password")
        else:
            self._password = password

    def _getUsername(self):
        return self._username

    def _getEmail(self):
        return self._email

    def _getPassword(self):
        #not sure if we ever want to return the password but i put it in
        return self._password

    def borrow(self, book):
        # Make sure the user is trying to borrow a book
        if isinstance(Book, book):
            if book.isAvailable():
                # Next two lines set the due date to be seven days
                # after the user borrows the book
                now = datetime.now()
                due_date = timedelta(days=+7)
                self.borrowlist[book] = now + due_date
                book._setAvailability(False)
