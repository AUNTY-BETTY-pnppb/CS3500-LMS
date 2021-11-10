import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter.constants import END
from Book import *
from User import *
import re
from Bookshelf import *
from datetime import datetime, timedelta

global demo_user
demo_user = User('Chris', 'chris@gmail.com', '1234')
demo_user.reservelist.append(Book('Genre', 'Name', 'ss'))
demo_user.borrowlist[Book('Genre', 'Name', 'ss')] = datetime.now().strftime("%d %b %Y")

class MainTK:
    # this class is for the tkinter stuff altogether
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Management System")
        self.style = ttk.Style(self.root)
        self.style.configure('lefttab.TNotebook', tabposition='wn')
        self._tab_bar = tk.ttk.Notebook(self.root, style='lefttab.TNotebook')
        self.profile = Profile(self._tab_bar)
        self.search = Search(self._tab_bar)
        self.borrow = Borrow(self._tab_bar)
        self.donate = Donate(self._tab_bar)
        self.tabControl()

    # adding the tabs
    def tabControl(self):
        self._tab_bar.add(self.profile.frame, text='Profile')
        self._tab_bar.add(self.search.frame, text='Search')
        self._tab_bar.add(self.borrow.frame, text='Borrow')
        self._tab_bar.add(self.donate.frame, text='Donate')
        self._tab_bar.grid(column=0, row=0)

class Profile:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        # list of books borrowed
        self._dueList = tk.Listbox(self.frame, height=15, width=40)
        self._reserveList = tk.Listbox(self.frame, height=7, width=40)

        # These are labels and titles for profile
        # REMINDER param of name is user's name
        self._name = tk.Label(self.frame, width=30, text=demo_user._getUsername())
        self._borrowedLabel =  tk.Label(self.frame, height=1, width=30, text="Borrowed Books")
        self._reservedLabel =  tk.Label(self.frame, height=1, width=30, text="Reserved Books")

        # blanks are whitespaces for better readability
        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self.positionWidgets()
        self.myBooks()
        self.myReservedBooks()

    def positionWidgets(self):
        # postition all widgets in frame
        self._name.grid(row=0, column=0, columnspan=4)

        self._borrowedLabel.grid(row=1, column=1)
        self._dueList.grid(row=2, column=1)

        self._reservedLabel.grid(row=1, column=3)
        self._reserveList.grid(row=2, column=3, sticky='n')

        self._blank.grid(row=2, column=2)
        self._blank1.grid(row=2, column=0)


    def myBooks(self):
        for book, date in demo_user.borrowlist.items():
            self._dueList.insert(END, book, date)

    def myReservedBooks(self):
        for book in demo_user.reservelist:
            self._reserveList.insert(END, book)

class Search:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        # the search buttton
        self._search = tk.Entry(self.frame, width=40)
        self._searchButton = tk.Button(self.frame, text="Search", command=self.searchEngine)

        # listboxes for input and entries
        self._searchList = tk.Listbox(self.frame, height=15, width=70)

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

        self._searchList.grid(row=3, column=1, columnspan=6)

        self._blank.grid(row=1, column=0)
        self._blank1.grid(row=2, column=0)
        self._blank2.grid(row=0, column=0)
        self._blank3.grid(row=3, column=7)
        self._blank4.grid(row=4, column=7)

    def searchEngine(self):
        self._searchList.delete(0, END)
        userInput = self._search.get() # Getting the search data
        print(userInput)
        self._searchList.delete(first=0, last=10000)
        for book in bookshelf.getKeys(bookshelf.bookList):
            item = bookshelf.search(bookshelf.bookList, book)
            match = re.search(": %s" % userInput.lower(), str(item).lower())
            print(match)
            if match:
                self._searchList.insert(END, bookshelf.search(bookshelf.bookList, book))
                print(match.string)


    def searchList(self):
        return

class Borrow:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._borrowReserveButton = tk.Button(self.frame, text="Borrow/Reserve", command=self.borrow)
        self._resetButton = tk.Button(self.frame, text="Reset", command=self.reset)

        self._borrowLabel =  tk.Label(self.frame, height=1, width=30, text="Borrowing")
        self._reservedLabel =  tk.Label(self.frame, height=1, width=30, text="Reserving")

        self._borrowList = tk.Listbox(self.frame, height=15, width=40)
        self._reserveList = tk.Listbox(self.frame, height=7, width=40)

        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)

        self.positionWidgets()

    def positionWidgets(self):
        # postition all widgets in frame
        self._borrowReserveButton.grid(row=3, column=3, sticky='nw')
        self._resetButton.grid(row=3, column=3, sticky='n')

        self._borrowLabel.grid(row=1, column=1)
        self._borrowList.grid(row=2, column=1, rowspan=5)

        self._reservedLabel.grid(row=1, column=3)
        self._reserveList.grid(row=2, column=3, columnspan=3, sticky='n')

        self._blank.grid(row=2, column=2)
        self._blank1.grid(row=0, column=2)
        self._blank2.grid(row=0, column=0)
        self._blank3.grid(row=0, column=6)

    def borrow(self, book):
        # Make sure the user is trying to borrow a book
        if book.isAvailable():
            # Next two lines set the due date to be seven days
            # after the user borrows the book
            now = datetime.now()
            due_date = timedelta(days=+7)
            demo_user.borrowlist[book] = now + due_date
            book._setAvailability(False)


    def reset(self):
        # reset the book lists to nothing
        return


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
        genreDictionary = {1: "Action", 2: "Romance", 3: "Fantasy", 4: "SciFi", 5: "Drama", 6: "Horror"}
        print(self._titleBox.get(), self._authorBox.get(), genreDictionary[self._var.get()])
        donatedBook = Book(genreDictionary[self._var.get()], self._titleBox.get(), self._authorBox.get())
        bookshelf = Bookshelf()
        bookshelf.insert(bookshelf.bookList, str(donatedBook._getBookId()), donatedBook)
        self.reset()

    def reset(self):
        # reset the book lists to nothing
        self._titleBox.delete(first=0, last=10000)
        self._authorBox.delete(first=0, last=10000)

if __name__ == "__main__":
    bookshelf = Bookshelf()
    ch = ["Chris", "1234", "chris@gmail.com"]
    bookshelf.insert(bookshelf.membersList, ch[0], ch)
    shelf = bookshelf.getKeys(bookshelf.membersList)
    print(bookshelf.search(bookshelf.membersList, "Chris"))
    # remember to close the shelves afterwards
    bookshelf.close(bookshelf.membersList)

    library = bookshelf.getKeys(bookshelf.bookList)
    for book in library:
        print(bookshelf.search(bookshelf.bookList, book))

app = MainTK()
app.root.mainloop()
