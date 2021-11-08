import tkinter as tk
from tkinter import PhotoImage, ttk
import shelve
import book
import user

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
        self._name = tk.Label(self.frame, width=30, text="default text")
        self._borrowedLabel =  tk.Label(self.frame, height=1, width=30, text="Borrowed Books")
        self._reservedLabel =  tk.Label(self.frame, height=1, width=30, text="Reserved Books")

        # blanks are whitespaces for better readability
        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self.positionWidgets()

    def positionWidgets(self):
        # postition all widgets in frame
        self._name.grid(row=0, column=0, columnspan=4)

        self._borrowedLabel.grid(row=1, column=1)
        self._dueList.grid(row=2, column=1)

        self._reservedLabel.grid(row=1, column=3)
        self._reserveList.grid(row=2, column=3, sticky='n')

        self._blank.grid(row=2, column=2)
        self._blank1.grid(row=2, column=0)

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
        userInput = self._search.get() # Getting the search data
        print(userInput)

    
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
    
    def borrow(self):
        # put your borrow and reserve here
        return
    
    def reset(self):
        # reset the book lists to nothing
        return

class Donate:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._donateButton = tk.Button(self.frame, text="Donate", command=self.donate)
        self._resetButton = tk.Button(self.frame, text="Reset", command=self.reset)

        self._donateList = tk.Listbox(self.frame, height=10, width=40)

        self._donateLabel = tk.Label(self.frame, height=1, width=30, text="Donating")


        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)

        self.positionWidgets()

    def positionWidgets(self):
        # postition all widgets in frame
        self._donateButton.grid(row=7, column=1, sticky='sw')
        self._resetButton.grid(row=7, column=1, sticky='se')

        self._donateLabel.grid(row=1, column=1)
        self._donateList.grid(row=2, column=1, rowspan=5)

        self._blank.grid(row=2, column=2)
        self._blank1.grid(row=0, column=2)
        self._blank2.grid(row=0, column=0)
        self._blank3.grid(row=0, column=6)

    def donate(self):
        # put your donate here
        return

    def reset(self):
        # reset the book lists to nothing
        return

class Bookshelf:

    def __init__(self):
        self.name = "Bookshelf"

    def getKeys(self):
        st = shelve.open(self.name)
        return st.keys()
    
    def close(self):
        st = shelve.open(self.name)
        st.close()

    def search(self, key):
        st = shelve.open(self.name)
        value = st[key]
        st.close()
        return value

    def insert(self, key, value):
        # value is a list, playlist
        st = shelve.open(self.name, writeback=True)
        st[key] = value
        st.close()
    
    def delete(self):
        st = shelve.open(self.name)
        for key in self.getKeys():
            del st[key]
        st.close()

app = MainTK()
app.root.mainloop()
