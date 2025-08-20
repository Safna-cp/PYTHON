books = ("To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice", "Moby Disign")
print(books)

book_list = list(books)

book_list.remove("Pride and Prejudice")
books = tuple(book_list)
print(books)


for item in books:
    print(item)

if "The Great Gatsby" in books:
    print("Yes The Great Gatsby is in books ")
else:
    print("Unfortunately not in list")


print("TOTAL NUMBER OF BOOK ", len(books))


