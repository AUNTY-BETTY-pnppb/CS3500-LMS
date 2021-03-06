import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter.constants import END
from Book import *
from User import *
import re
from Bookshelf import *
from datetime import datetime, timedelta
global app

class MainTK:
    # this class is for the tkinter stuff altogether
    def __init__(self, user):
        self.user = user
        self.root = tk.Tk()
        self.root.title("Library Management System")
        self.style = ttk.Style(self.root)
        self.style.configure('lefttab.TNotebook', tabposition='wn')
        self._tab_bar = tk.ttk.Notebook(self.root, style='lefttab.TNotebook')
        self.profile = Profile(self._tab_bar, user)
        self.search = Search(self._tab_bar)
        self.borrow = Borrow(self._tab_bar, user)
        self.donate = Donate(self._tab_bar)
        self.tabControl()
        self.root.protocol("WM_DELETE_WINDOW", self.logout)

    # adding the tabs
    def tabControl(self):
        self._tab_bar.add(self.profile.frame, text='Profile')
        self._tab_bar.add(self.search.frame, text='Search')
        self._tab_bar.add(self.borrow.frame, text='Borrow')
        self._tab_bar.add(self.donate.frame, text='Donate')
        self._tab_bar.grid(column=0, row=0)

    def logout(self):
        start.root.deiconify()
        self.root.destroy()

class Profile:
    def __init__(self, parent, user):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self.user = user

        # list of books borrowed
        self._dueList = tk.Listbox(self.frame, height=15, width=40)
        self._reserveList = tk.Listbox(self.frame, height=7, width=40)
        #Button
        self._refreshButton = tk.Button(self.frame, text="Refresh", command=self.refresh)
        self._returnButton = tk.Button(self.frame, text="Return Book", command=self.returnBook)
        self._cancelButton = tk.Button(self.frame, text="Cancel Reservation", command=self.cancel)
        self._logoutButton = tk.Button(self.frame, text="Logout", command=self.logout)
        # These are labels and titles for profile
        # REMINDER param of name is user's name
        self._name = tk.Label(self.frame, width=30, text=self.user._getUsername(), font=20)
        self._borrowedLabel =  tk.Label(self.frame, height=1, width=30, text="Borrowed Books")
        self._reservedLabel =  tk.Label(self.frame, height=1, width=30, text="Reserved Books")

        self._responseLabel = tk.Label(self.frame, height=1, text="")

        # blanks are whitespaces for better readability
        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self.positionWidgets()
        self.myBooks()
        self.myReservedBooks()

    def positionWidgets(self):
        # postition all widgets in frame
        self._name.grid(row=0, column=0, columnspan=4)
        self._refreshButton.grid(row=4, column=3, sticky='nw')
        self._returnButton.grid(row=3, column=3, sticky='nw')
        self._cancelButton.grid(row=3, column=3, sticky='ne')
        self._logoutButton.grid(row=5, column=3, sticky='ne')

        self._borrowedLabel.grid(row=1, column=1)
        self._dueList.grid(row=2, column=1, rowspan=4)

        self._reservedLabel.grid(row=1, column=3)
        self._reserveList.grid(row=2, column=3, columnspan=3, sticky='n')

        self._responseLabel.grid(row=6, column=3, sticky='w', columnspan=3)

        self._blank.grid(row=2, column=2)
        self._blank1.grid(row=2, column=0)


    def myBooks(self):
        self._dueList.delete(0, END)
        if not self.user.borrowList:
            self._dueList.insert(END, "No currently borrowed books")
        else:
            for book, date in self.user.borrowList.items():
                self._dueList.insert(END,"%s %s" % (book, date))

    def myReservedBooks(self):
        self._reserveList.delete(0, END)
        if not self.user.reserveList:
            self._reserveList.insert(END, "No currently reserved books")
        else:
            for book in self.user.reserveList:
                self._reserveList.insert(END, "%s %s" % (book[0], book[1]))

    def refresh(self):
        self.myBooks()
        self.myReservedBooks()

    def returnBook(self):
        bookToReturn = self._dueList.get(self._dueList.curselection())
        bookshelf = Bookshelf()
        for book1, date in self.user.borrowList.items():
            # Check for match, book1 is an object hence the str.
            # Have to add 2 strings because the date was added
            # to the object that was borrowed
            book = bookshelf.search(bookshelf.bookList, str(book1[1]))
            bookDetails = bookToReturn.split(", ")
            print(bookDetails)
            bookID = bookDetails[1][:13]
            if str(book1[1]) in bookID:
                bookID.strip(")")
                bookID = book._getBookId()
                book._setAvailability(True)
                bookshelf.insert(bookshelf.bookList, str(bookID), book)
                self.user.borrowList.pop(book1)
                for user in bookshelf.getKeys(bookshelf.membersList):
                    possibleUser = bookshelf.search(bookshelf.membersList, user)
                    if possibleUser._getUsername() == self.user._getUsername():
                        bookshelf.insert(bookshelf.membersList, possibleUser._getUsername(), self.user)
                self._responseLabel.config(text="You returned %s" % book.getName())
                app.search.searchEngine()
                break
        #Update
        self.myBooks()

    def cancel(self):
        #find the highlighted book
        bookToCancel = self._reserveList.get(self._reserveList.curselection())
        bookshelf = Bookshelf()
        for book in self.user.reserveList:
            # Check for match, book1 is an object hence the str
            #print(book[1])
            book1 = bookshelf.search(bookshelf.bookList, str(book[1]))
            #print(book1)
            if book[1] == book1._getBookId():
                print("match")
                self.user.reserveList.remove(book)
                for user in bookshelf.getKeys(bookshelf.membersList):
                    possibleUser = bookshelf.search(bookshelf.membersList, user)
                    if possibleUser._getUsername() == self.user._getUsername():
                        bookshelf.insert(bookshelf.membersList, possibleUser._getUsername(), self.user)
                self._responseLabel.config(text="You cancelled the reservation on %s" % book1.getName())
        #Update
        self.myReservedBooks()

    def logout(self):
        start.root.deiconify()
        app.root.destroy()

class Search:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        # the search buttton
        self._search = tk.Entry(self.frame, width=40)
        self._searchButton = tk.Button(self.frame, text="Search", command=self.searchEngine)

        self._genreVar = tk.StringVar()
        self._genreVar.set("All") # default value

        self._genreMenu = tk.OptionMenu(self.frame, self._genreVar, "All", "Action", "Romance", "Fantasy", "Sci-fi", "Drama", "Horror")

        # listboxes for input and entries
        self._searchList = tk.Listbox(self.frame, height=15, width=80)
        self._searchList.bind('<Double-1>', self.borrow)
        self.listAll()

        # Blanks again
        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)
        self._blank4 = tk.Label(self.frame, height=1, width=5)


        self.positionWidgets()

    def positionWidgets(self):
        # postition all widgets in frame
        self._search.grid(row=1, column=1, columnspan=4)
        self._searchButton.grid(row=1, column=5, sticky='nw')

        self._genreMenu.grid(row=1, column=6, sticky='nw')

        self._searchList.grid(row=3, column=1, columnspan=6)

        self._blank.grid(row=1, column=0)
        self._blank1.grid(row=2, column=0)
        self._blank2.grid(row=0, column=0)
        self._blank3.grid(row=3, column=7)
        self._blank4.grid(row=4, column=7)

    def searchEngine(self):
        self._searchList.delete(0, END)
        userInput = self._search.get() # Getting the search data
        #print(userInput)
        # Yo dave i switched them around so that if the bar is empty
        # it will return all books
        # PROBLEM - the search will return wrong entries when i enter one letter
        # if i enter "h" in the search i get:
        # hardyhar
        # hooligan
        # can you feel the love tonight
        # i get the last one because of "the" and "tonight" having "h"
        if userInput == "":
            self.listAll()

        else:
            genre = self._genreVar.get()
            for book in bookshelf.getKeys(bookshelf.bookList):
                item = bookshelf.search(bookshelf.bookList, book)
                matchName = re.search("^%s" % userInput.lower(), item.getName().lower())
                matchAuthor = re.search("^%s" % userInput.lower(), item.getAuthor().lower())
                if genre == "All":
                    if matchName or matchAuthor:
                        self._searchList.insert(END, item)
                elif genre == item.getGenre():
                    if matchName or matchAuthor:
                        self._searchList.insert(END, item)

    def listAll(self):
        genre = self._genreVar.get()
        #print(genre)
        for book in bookshelf.getKeys(bookshelf.bookList):
            item = bookshelf.search(bookshelf.bookList, book)
            if genre == "All":
                self._searchList.insert(END, item)
            elif genre == item.getGenre():
                self._searchList.insert(END, item)

    def borrow(self, event):
        selected = event.widget
        if selected.curselection():
            index = int(selected.curselection()[0])
            book = selected.get(index)
            bookObj = self.searchList(book)
            # Checks for if the book is available
            #app.borrow.borrow(bookObj)
            if bool(bookObj._getAvailability()):
                app.borrow._borrowList.insert(END,"%s" % bookObj)
            else:
                app.borrow._reserveList.insert(END,"%s" % bookObj)

            #print(type(bookObj))

    def searchList(self, selected):
        for book in bookshelf.getKeys(bookshelf.bookList):
            item = bookshelf.search(bookshelf.bookList, book)
            if str(item) == str(selected):
                return item

class Borrow:
    def __init__(self, parent, user):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self.user = user

        self._borrowButton = tk.Button(self.frame, text="Borrow", command=self.borrow)
        self._reserveButton = tk.Button(self.frame, text="Reserve", command=self.reserve)
        self._resetButton = tk.Button(self.frame, text="Reset", command=self.reset)

        self._borrowLabel =  tk.Label(self.frame, height=1, width=30, text="Borrowing")
        self._reservedLabel =  tk.Label(self.frame, height=1, width=30, text="Reserving")

        self._responseLabel = tk.Label(self.frame, height=1, text="")

        self._borrowList = tk.Listbox(self.frame, height=15, width=40)
        self._reserveList = tk.Listbox(self.frame, height=7, width=40)

        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)

        self.positionWidgets()

    def positionWidgets(self):
        # postition all widgets in frame
        self._borrowButton.grid(row=3, column=3, sticky='nw')
        self._reserveButton.grid(row=3, column=3, sticky='n')
        self._resetButton.grid(row=3, column=3, sticky='ne')

        self._borrowLabel.grid(row=1, column=1)
        self._borrowList.grid(row=2, column=1, rowspan=5)

        self._reservedLabel.grid(row=1, column=3)
        self._reserveList.grid(row=2, column=3, columnspan=3, sticky='n')

        self._responseLabel.grid(row=4, column=3, sticky='w', columnspan=3)

        self._blank.grid(row=2, column=2)
        self._blank1.grid(row=0, column=2)
        self._blank2.grid(row=0, column=0)
        self._blank3.grid(row=0, column=6)

    def borrow(self):
        bookToBorrow = self._borrowList.get(self._borrowList.curselection())
        # deletes the entry from the borrow list
        index = int(self._borrowList.curselection()[0])
        self._borrowList.delete(index)

        book = app.search.searchList(bookToBorrow)
        bookshelf = Bookshelf()
        bookID = book._getBookId()
        # Next two lines set the due date to be seven days
        # after the user borrows the book
        now = datetime.now()
        due_on = timedelta(days=+7)
        due_date = now + due_on
        # app is the MainTK where all other tk classes resolve
        # so to call stuff in other classes must go - app.class._objectButton
        for user in bookshelf.getKeys(bookshelf.membersList):
            possibleUser = bookshelf.search(bookshelf.membersList, user)
            if possibleUser._getUsername() == self.user._getUsername():
                self.user.borrowList[book.getName(), book._getBookId()] = due_date.strftime("%d %b %Y")
                book._setAvailability(False)
                bookshelf.insert(bookshelf.bookList, str(bookID), book)
                bookshelf.insert(bookshelf.membersList, possibleUser._getUsername(), self.user)
        app.profile.myBooks()
        self._responseLabel.config(text="You borrowed %s" % book.getName())
        app.search.searchEngine()


    def reset(self):
        # reset the book lists to nothing
        self._borrowList.delete(0, END)
        self._reserveList.delete(0, END)

    def reserve(self):
        bookToReserve = self._reserveList.get(self._reserveList.curselection())
        index = int(self._reserveList.curselection()[0])
        self._reserveList.delete(index)
        book = app.search.searchList(bookToReserve)
        for user in bookshelf.getKeys(bookshelf.membersList):
            possibleUser = bookshelf.search(bookshelf.membersList, user)
            if possibleUser._getUsername() == self.user._getUsername():
                self.user.reserveList.append((book.getName(), book._getBookId()))
                bookshelf.insert(bookshelf.membersList, possibleUser._getUsername(), self.user)
        # Next two lines set the due date to be seven days
        # after the user borrows the book
        # app is the MainTK where all other tk classes resolve
        # so to call stuff in other classes must go - app.class._objectButton
        app.profile.myReservedBooks()
        self._responseLabel.config(text="You reserved %s" % book.getName())

class Donate:
    def __init__(self, parent):
        # Create parent, frame
        self._var = tk.IntVar()

        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._donateButton = tk.Button(self.frame, text="Donate", command=self.donate)
        self._resetButton = tk.Button(self.frame, text="Reset", command=self.reset)

        self._titleBox = tk.Entry(self.frame, width=40)
        self._authorBox = tk.Entry(self.frame, width=40)
        self._genreAction = tk.Radiobutton(self.frame, text="Action", variable=self._var, value=1)
        self._genreRomance = tk.Radiobutton(self.frame, text="Romance", variable=self._var, value=2)
        self._genreFantasy = tk.Radiobutton(self.frame, text="Fantasy", variable=self._var, value=3)
        self._genreSciFi = tk.Radiobutton(self.frame, text="SciFi", variable=self._var, value=4)
        self._genreDrama = tk.Radiobutton(self.frame, text="Drama", variable=self._var, value=5)
        self._genreHorror = tk.Radiobutton(self.frame, text="Horror", variable=self._var, value=6)

        self._titleLabel = tk.Label(self.frame, height=1, width=10, text="Title:")
        self._authorLabel = tk.Label(self.frame, height=1, width=10, text="Author:")
        self._genreLabel = tk.Label(self.frame, height=1, width=10, text="Genre:")

        self._responseLabel = tk.Label(self.frame, height=1, text="")

        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)

        self.positionWidgets()


    def positionWidgets(self):
        # position all widgets in frame
        self._donateButton.grid(row=2, column=4, sticky='w', padx=10)
        self._resetButton.grid(row=1, column=4, sticky='w', padx=10)

        self._titleLabel.grid(row=1, column=1, sticky='w')
        self._titleBox.grid(row=1, column=2, columnspan=2, sticky='w')

        self._authorLabel.grid(row=2, column=1, sticky='w')
        self._authorBox.grid(row=2, column=2, columnspan=2, sticky='w')

        self._responseLabel.grid(row=6, column=1, sticky='w', columnspan=5)

        self._genreLabel.grid(row=3, column=1, sticky='w')
        self._genreAction.grid(row=3, column=2, sticky='w')
        self._genreRomance.grid(row=4, column=2, sticky='w')
        self._genreFantasy.grid(row=5, column=2, sticky='w')
        self._genreSciFi.grid(row=3, column=3, sticky='w')
        self._genreDrama.grid(row=4, column=3, sticky='w')
        self._genreHorror.grid(row=5, column=3, sticky='w')

        self._blank.grid(row=0, column=1)
        self._blank1.grid(row=0, column=1)
        self._blank2.grid(row=0, column=0)
        self._blank3.grid(row=0, column=6)

    def donate(self):
        # put your donate here

        genreDictionary = {1: "Action", 2: "Romance", 3: "Fantasy", 4: "Sci-fi", 5: "Drama", 6: "Horror"}
        print(self._titleBox.get(), self._authorBox.get(), genreDictionary[self._var.get()])
        donatedBook = Book(genreDictionary[self._var.get()], self._titleBox.get(), self._authorBox.get())
        bookshelf = Bookshelf()
        bookshelf.insert(bookshelf.bookList, str(donatedBook._getBookId()), donatedBook)
        self._responseLabel.config(text="Thank you for donating %s to our library!" % (self._titleBox.get()))
        self.reset()

    def reset(self):
        # reset the book lists to nothing
        self._titleBox.delete(first=0, last=10000)
        self._authorBox.delete(first=0, last=10000)

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
        self._passwordBox = tk.Entry(self.frame, show='*', width=40)

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
        if self._usernameBox.get() and self._passwordBox.get():
            for member in bookshelf.getKeys(bookshelf.membersList):
                if member == self._usernameBox.get():
                    print(member)
                    account = bookshelf.search(bookshelf.membersList, self._usernameBox.get())
                    if account._getPassword() == self._passwordBox.get():
                        quitAccessTK(account)
        else:
            self._responseLabel.config(text="User invalid")

class SignUp:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._title = tk.Label(self.frame, height=1, text="Sign Up", font=20)
        self._signUpButton = tk.Button(self.frame, text="Sign Up", command=self.createAccount)

        self._usernameBox = tk.Entry(self.frame, width=40)
        self._passwordBox = tk.Entry(self.frame, show='*', width=40)
        self._emailBox = tk.Entry(self.frame, width=40)

        self._usernameLabel = tk.Label(self.frame, height=1, width=10, text="Username :")
        self._passwordLabel = tk.Label(self.frame, height=1, width=10, text="Password :")
        self._emailLabel = tk.Label(self.frame, height=1, width=10, text="Email :")

        self._responseLabel = tk.Label(self.frame, height=1, text="")

        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)
        self._blank4 = tk.Label(self.frame, height=1, width=5)
        self._blank5 = tk.Label(self.frame, height=1, width=5)
        self._blank6 = tk.Label(self.frame, height=1, width=5)

        self.positionWidgets()


    def positionWidgets(self):
        # position all widgets in frame
        self._signUpButton.grid(row=9, column=4, sticky='w', padx=10)
        self._title.grid(row=1, column=4)

        self._usernameLabel.grid(row=3, column=1, sticky='w')
        self._usernameBox.grid(row=3, column=2, columnspan=5, sticky='w')

        self._passwordLabel.grid(row=5, column=1, sticky='w')
        self._passwordBox.grid(row=5, column=2, columnspan=5, sticky='w')

        self._emailLabel.grid(row=7, column=1, sticky='w')
        self._emailBox.grid(row=7, column=2, columnspan=5, sticky='w')

        self._responseLabel.grid(row=10, column=1, sticky='w', columnspan=9)

        self._blank.grid(row=0, column=1)
        self._blank1.grid(row=6, column=1)
        self._blank2.grid(row=3, column=0)
        self._blank3.grid(row=4, column=7)
        self._blank4.grid(row=2, column=4)
        self._blank5.grid(row=8, column=4)
        self._blank6.grid(row=11, column=4)

    def createAccount(self):
        if self._usernameBox.get() and not bool(re.search(r'\d', self._usernameBox.get())):
            if bool(re.search(r'\d', self._passwordBox.get())) and len(self._passwordBox.get()) > 8:
                newAccount = User(self._usernameBox.get(), self._passwordBox.get(), self._emailBox.get())
                bookshelf.insert(bookshelf.membersList, self._usernameBox.get(), newAccount)
                print(newAccount)
                quitAccessTK(newAccount)
            else:
                self._responseLabel.config(text="Password must be 8 characters long and have a number")
        else:
            self._responseLabel.config(text="Username is invalid")


class Retrieve:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._title = tk.Label(self.frame, height=1, text="Forgotten Password", font=20)
        self._retrieveButton = tk.Button(self.frame, text="Get password", command=self.retrievePassword)

        self._usernameBox = tk.Entry(self.frame, width=40)

        self._usernameLabel = tk.Label(self.frame, height=1, width=10, text="Email")

        self._responseLabel = tk.Label(self.frame, height=1, text="Enter your email to retrieve your password")

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

    def retrievePassword(self):
        userEmail = self._usernameBox.get()
        if userEmail == "":
            self._responseLabel.config(text="We can't send you your password without your email address")

        else:
            for user in bookshelf.getKeys(bookshelf.membersList):
                possibleUser = bookshelf.search(bookshelf.membersList, user)
                if possibleUser._getEmail() == userEmail:
                    self._responseLabel.config(text="Your password is %s" % possibleUser._getPassword())
                    return
            self._responseLabel.config(text="You are not a member of our Library. Please sign up to get started")


def quitAccessTK(user) :
    global app
    start.root.withdraw()
    app = MainTK(user)
    app.root.mainloop()


bookshelf = Bookshelf()

start = AccessTK()
start.root.mainloop()
