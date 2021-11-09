import shelve

class Bookshelf:

    def __init__(self):
        # all the lists of shelves
        self.booklist = "booklist"
        self.memberslist = "memberslist"

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

    def delete(self):
        st = shelve.open(self.name)
        for key in self.getKeys():
            del st[key]
        st.close()