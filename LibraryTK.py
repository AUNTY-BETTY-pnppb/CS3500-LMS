import tkinter as tk
from tkinter import PhotoImage, ttk

class MainTK:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Library Management System")
        self.style = ttk.Style(self.root)
        self.style.configure('lefttab.TNotebook', tabposition='wn')
        self._tab_bar = tk.ttk.Notebook(self.root, style='lefttab.TNotebook')
        self.profile = Profile(self._tab_bar)
        self.search = Search(self._tab_bar)
        self.tabControl()

    def tabControl(self):
        self._tab_bar.add(self.profile.frame, text='Profile')
        self._tab_bar.add(self.search.frame, text='Search')
        self._tab_bar.grid(column=0, row=0)

class Profile:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)
        
        # list of books borrowed
        self._duelist = tk.Listbox(self.frame, height=15, width=50, bg="white")

        # REMINDER param of name is user's name
        self._name = tk.Label(self.frame, width=30, text="default text", bg="white")
        self._dlabel =  tk.Label(self.frame, height=1, width=50, text="Borrowed Books", bg="green")
        self.pos_widgets()

    def pos_widgets(self):
        # postition all widgets in frame
        
        self._name.grid(row=0, column=1)
        self._duelist.grid(row=2, column=1)
        self._dlabel.grid(row=1, column=1)
        

class Search:
    def __init__(self, parent):
        # Create parent, frame
        self._parent = parent
        self.frame = tk.Frame(self._parent)

    def pos_widgets(self):
        # postition all widgets in frame
        return

app = MainTK()
app.root.mainloop()
















