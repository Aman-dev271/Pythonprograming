
import time
input_search_What = input("Enter the latter that you wan to search\n")
def searcher():
    new = open("amannew.txt","r")
    book_inside = (new.read())

    time.sleep(4)
    while True:
        input_search_What = input("Enter the latter that you wan to search\n")
        input_search_What = (yield)
        if input_search_What in book_inside:
            print(f"your world {input_search_What} is in the book")
        else:
            print(f"your world {input_search_What} is not in the book")
text_search = searcher()
next(text_search)
text_search.send(input_search_What)
# next(text_search)
text_search.send(input_search_What)
