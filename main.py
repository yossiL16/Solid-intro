# from s.book import Book
# from s.SavingFile import SavingFile
# from s.gradeCalculator import GradeCalculator
# from s.student import Student
from s.order import Order, Print

# s1
# book = Book("hari potter", "j k roling", "oufwhlkeuhlku")
# save_file = SavingFile.save_to_file(book.title, book)

# s2
# if __name__ == "__main__":
    # student = Student("yossi", [100, 98, 92, 93, 89, 70, 88])
    # GradeCalculator.average_grade(student)

# s3
order = Order(["banana", "apple", "melon"], 43.6)
Print.print_invoice(order.items, order.total_price)

