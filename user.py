class User:

    def __init__(self, username, email, password):
        #will need a check to shelf to see if an existing user
        #or email exists when creating a new user

    def __str__(self):
        return '%s %s' % (self._username, self._email)

    def _set_username(self, username):
        #check shelf again for existing
        if type(username) != str:
            print("Invalid username")
        else:
            self._username = username

    def _set_email(self, email):
        #check shelf again for existing
        if type(name) != str:
            print("Invalid email")
        else:
            self._email = email

    def _set_password(self, password):
        # some check if we want to have a password eg. 8chars long etc...
        if type(password) != str:
            print("invalid password")
        else:
            self._password = password

    def _get_username(self):
        return self._username

    def _get_email(self):
        return self._email

    def _get_password(self):
        #not sure if we ever want to return the password but i put it in
        return self._password
