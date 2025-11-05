from book import Book

class SavingFile:

    @staticmethod
    def save_to_file(filename, book:Book):
        with open(filename, "w") as f:
            f.write(book.content)