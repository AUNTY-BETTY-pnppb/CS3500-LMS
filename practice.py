from Bookshelf import *
print("yo PRINT")
shelf = Bookshelf()
shelf.delete(shelf.bookList)
sh = shelf.getKeys(shelf.bookList)

for item in sh:
    print(item, end = " - ")
    key = shelf.search(shelf.bookList, item)
    print(key)
