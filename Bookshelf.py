import shelve

class Bookshelf:

    def __init__(self):
        # all the lists of shelves
        self.bookList = "bookList"
        self.membersList = "membersList"

    def getKeys(self, shelf):
        st = shelve.open(shelf)
        return st.keys()

    def close(self, shelf):
        st = shelve.open(shelf)
        st.close()

    def search(self, shelf, key):
        st = shelve.open(shelf)
        value = st[key]
        st.close()
        return value

    def insert(self, shelf, key, value):
        # value is a list, playlist
        st = shelve.open(shelf, writeback=True)
        st[key] = value
        st.close()

    def delete(self, shelf):
        st = shelve.open(shelf)
        for key in self.getKeys(shelf):
            del st[key]
        st.close()

bookshelf = Bookshelf()
for book in bookshelf.getKeys(bookshelf.bookList):
    print(str(book))
