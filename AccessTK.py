import tkinter as tk
from tkinter import READABLE, PhotoImage, ttk
from tkinter.constants import END
from Book import *
from User import *

class AccessTK:
    # this class is for the tkinter stuff altogether
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Management System")
        self.style = ttk.Style(self.root)
        self.style.configure('lefttab.TNotebook', tabposition='wn')
        self._tab_bar = tk.ttk.Notebook(self.root, style='lefttab.TNotebook')
        self.login = Login(self._tab_bar)
        self.signUp = SignUp(self._tab_bar)
        self.retrieve = Retrieve(self._tab_bar)
        self.tabControl()

    # adding the tabs
    def tabControl(self):
        self._tab_bar.add(self.login.frame, text='Login')
        self._tab_bar.add(self.signUp.frame, text='Sign up')
        self._tab_bar.add(self.retrieve.frame, text='Retrieve')
        self._tab_bar.grid(column=0, row=0)

class Login:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._title = tk.Label(self.frame, height=1, text="Login", font=20)
        self._loginButton = tk.Button(self.frame, text="Login", command=self.login)

        self._usernameBox = tk.Entry(self.frame, width=40)
        self._passwordBox = tk.Entry(self.frame, width=40)

        self._usernameLabel = tk.Label(self.frame, height=1, width=10, text="Username")
        self._passwordLabel = tk.Label(self.frame, height=1, width=10, text="Password")

        self._responseLabel = tk.Label(self.frame, height=1, text="")

        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)
        self._blank4 = tk.Label(self.frame, height=1, width=5)

        self.positionWidgets()


    def positionWidgets(self):
        # position all widgets in frame
        self._loginButton.grid(row=8, column=4, sticky='w', padx=10)
        self._title.grid(row=1, column=4)

        self._usernameLabel.grid(row=3, column=1, sticky='w')
        self._usernameBox.grid(row=3, column=2, columnspan=5, sticky='w')

        self._passwordLabel.grid(row=5, column=1, sticky='w')
        self._passwordBox.grid(row=5, column=2, columnspan=5, sticky='w')

        self._responseLabel.grid(row=9, column=1, sticky='w', columnspan=5)

        self._blank.grid(row=0, column=1)
        self._blank1.grid(row=7, column=1)
        self._blank2.grid(row=3, column=0)
        self._blank3.grid(row=4, column=7)
        self._blank4.grid(row=2, column=4)
    
    def login(self):
        pass

class SignUp:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._title = tk.Label(self.frame, height=1, text="Sign Up", font=20)
        self._signUpButton = tk.Button(self.frame, text="Sign Up", command=self.createAccount)

        self._usernameBox = tk.Entry(self.frame, width=40)
        self._passwordBox = tk.Entry(self.frame, width=40)

        self._usernameLabel = tk.Label(self.frame, height=1, width=10, text="Username")
        self._passwordLabel = tk.Label(self.frame, height=1, width=10, text="Password")

        self._responseLabel = tk.Label(self.frame, height=1, text="")

        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)
        self._blank4 = tk.Label(self.frame, height=1, width=5)

        self.positionWidgets()


    def positionWidgets(self):
        # position all widgets in frame
        self._signUpButton.grid(row=8, column=4, sticky='w', padx=10)
        self._title.grid(row=1, column=4)

        self._usernameLabel.grid(row=3, column=1, sticky='w')
        self._usernameBox.grid(row=3, column=2, columnspan=5, sticky='w')

        self._passwordLabel.grid(row=5, column=1, sticky='w')
        self._passwordBox.grid(row=5, column=2, columnspan=5, sticky='w')

        self._responseLabel.grid(row=9, column=1, sticky='w', columnspan=5)

        self._blank.grid(row=0, column=1)
        self._blank1.grid(row=7, column=1)
        self._blank2.grid(row=3, column=0)
        self._blank3.grid(row=4, column=7)
        self._blank4.grid(row=2, column=4)
    
    def createAccount(self):
        pass

class Retrieve:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._title = tk.Label(self.frame, height=1, text="Forgotten Password", font=20)
        self._retrieveButton = tk.Button(self.frame, text="Get password", command=self.createAccount)

        self._usernameBox = tk.Entry(self.frame, width=40)

        self._usernameLabel = tk.Label(self.frame, height=1, width=10, text="Email")

        self._responseLabel = tk.Label(self.frame, height=1, text="We will send you an email to retrieve your password")

        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)

        self.positionWidgets()


    def positionWidgets(self):
        # position all widgets in frame
        self._retrieveButton.grid(row=8, column=4, sticky='e', padx=10, pady=10)
        self._title.grid(row=1, column=4, padx=10, pady=10)

        self._usernameLabel.grid(row=3, column=1, sticky='w')
        self._usernameBox.grid(row=3, column=2, columnspan=4, sticky='w')

        self._responseLabel.grid(row=9, column=1, sticky='w', columnspan=5, padx=10, pady=10)

        self._blank.grid(row=0, column=1)
        self._blank1.grid(row=0, column=0)
    
    def createAccount(self):
        pass

app = AccessTK()
app.root.mainloop()