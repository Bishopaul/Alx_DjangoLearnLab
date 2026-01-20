# CRUD Operations

## Create
python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<Book: Book object (1)>

## Retrieve

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
1984 George Orwell 1949

## Update

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
Nineteen Eighty-Four

## Delete

book.delete()
print(Book.objects.all())
<QuerySet []>
