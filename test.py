import re

words = open("words.txt", "r")
words = words.readlines()

def search_engine(aList):
    userInput = input("Search: ")
    for item in aList:
        match = re.search("%s" % userInput, item)
        if match:   
            print(match.string)
    return 

search_engine(words)