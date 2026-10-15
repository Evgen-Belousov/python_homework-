"""
Этот модуль содержит реализацию для работы с списком книг.
Он предоставляет функциональность для добавления, удаления и получения книг.
"""

from book import Book


book1 = Book("Sam Gun", "Jeck London")
book2 = Book("Black", "Jon Lee")
book3 = Book("Scan", "Flip Anders")


library = [book1, book2, book3]
for book in library:
    print(f"{book.name} - {book.author}")
