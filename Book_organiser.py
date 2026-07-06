# Creating a list of books and printing basic information
books = ["Matilda", "Harry Porter", "Wonder", "Charlotte's Web", "The Jungle Book"]
print(len(books))
print(books[0])
print(books[-1])
print(books[2:4])

# Using some methods of list like append(), remove(), sort(), reverse() etc.
books.append("The Diary of a Wimpy Kid")
print(books)
books.remove("The Jungle Book")
print(books)
books.sort()
print(books)
books.sort(reverse = True)
print(books)
books.reverse()
print(books)

# creating a dictionary named librarian
librarian = {
    "name":"Ms.Priya",
    "Section":"Chidren's Books",
    "Experience":"5"
             }
# Changing the details of the librarian
print(librarian["name"])
librarian["Experience"] = 10
librarian["Email"] = "priya@schoollibrary.com"
librarian.pop("Section")
print(librarian)

Book_id = [100,101,102,103,104]
Book_names = ["Matilda", "Harry Porter", "Wonder", "Charlotte's Web", "The Diary of a Wimpy Kid"]
Book_directory = dict(zip(Book_id, Book_names))

# Printing the Summary
print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book Id Directory:", Book_directory)