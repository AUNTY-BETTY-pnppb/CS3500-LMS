from Book import *

class User:

    def __init__(self, username, password, email):
        #will need a check to shelf to see if an existing user
        #or email exists when creating a new user
        self._username = username
        self._password = password
        self._email = email
        self.borrowList = {}
        self.reserveList = []

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
