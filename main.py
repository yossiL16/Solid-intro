from s.book import Book
from s.SavingFile import SavingFile

#s1
book = Book("hari potter", "j k roling", "oufwhlkeuhlku")
save_file = SavingFile.save_to_file(book.title, book)