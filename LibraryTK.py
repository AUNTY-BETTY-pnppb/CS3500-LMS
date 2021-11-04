import tkinter as tk
from tkinter import PhotoImage, ttk
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
        self.tabControl()

    # adding the tabs
    def tabControl(self):
        self._tab_bar.add(self.profile.frame, text='Profile')
        self._tab_bar.add(self.search.frame, text='Search')
        self._tab_bar.add(self.borrow.frame, text='Borrow')
        self._tab_bar.grid(column=0, row=0)

class Profile:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)
        
        # list of books borrowed
        self._duelist = tk.Listbox(self.frame, height=15, width=40)
        self._reservelist = tk.Listbox(self.frame, height=7, width=40)

        # These are labels and titles for profile
        # REMINDER param of name is user's name
        self._name = tk.Label(self.frame, width=30, text="default text")
        self._dlabel =  tk.Label(self.frame, height=1, width=30, text="Borrowed Books")
        self._rlabel =  tk.Label(self.frame, height=1, width=30, text="Reserved Books")

        # blanks are whitespaces for better readability
        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self.pos_widgets()

    def pos_widgets(self):
        # postition all widgets in frame
        self._name.grid(row=0, column=0, columnspan=4)

        self._dlabel.grid(row=1, column=1)
        self._duelist.grid(row=2, column=1)

        self._rlabel.grid(row=1, column=3)
        self._reservelist.grid(row=2, column=3, sticky='n')

        self._blank.grid(row=2, column=2)
        self._blank1.grid(row=2, column=0)

class Search:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        # the search buttton
        self._search = tk.Entry(self.frame, width=40)
        self._sbtn = tk.Button(self.frame, text="Search", command=self.search_engine)

        # listboxes for input and entries
        self._searchlist = tk.Listbox(self.frame, height=15, width=70)

        # Blanks again
        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)
        self._blank4 = tk.Label(self.frame, height=1, width=5)
        

        self.pos_widgets()

    def pos_widgets(self):
        # postition all widgets in frame
        self._search.grid(row=1, column=1, columnspan=4)
        self._sbtn.grid(row=1, column=5, sticky='nw')

        self._searchlist.grid(row=3, column=1, columnspan=6)

        self._blank.grid(row=1, column=0)
        self._blank1.grid(row=2, column=0)
        self._blank2.grid(row=0, column=0)
        self._blank3.grid(row=3, column=7)
        self._blank4.grid(row=4, column=7)

    def search_engine(self):
        print("Searching... ")
    
    def search_list(self):
        return

class Borrow:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

        self._brbtn = tk.Button(self.frame, text="Borrow/Reserve", command=self.borrow)
        self._resetbtn = tk.Button(self.frame, text="Reset", command=self.reset)
        
        self._blabel =  tk.Label(self.frame, height=1, width=30, text="Borrowing")
        self._rlabel =  tk.Label(self.frame, height=1, width=30, text="Reserving")
        
        self._borrowlist = tk.Listbox(self.frame, height=15, width=40)
        self._reslist = tk.Listbox(self.frame, height=7, width=40)

        self._blank = tk.Label(self.frame, height=1, width=5)
        self._blank1 = tk.Label(self.frame, height=1, width=5)
        self._blank2 = tk.Label(self.frame, height=1, width=5)
        self._blank3 = tk.Label(self.frame, height=1, width=5)

        self.pos_widgets()

    def pos_widgets(self):
        # postition all widgets in frame
        self._brbtn.grid(row=3, column=3, sticky='nw')
        self._resetbtn.grid(row=3, column=3, sticky='n')

        self._blabel.grid(row=1, column=1)
        self._borrowlist.grid(row=2, column=1, rowspan=5)

        self._rlabel.grid(row=1, column=3)
        self._reslist.grid(row=2, column=3, columnspan=3, sticky='n')

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

app = MainTK()
app.root.mainloop()
