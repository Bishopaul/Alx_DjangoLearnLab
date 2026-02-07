from django.db import models
from django.db import models
from datetime import datetime

# Author model represents a writer who can have multiple books.
# This is the parent in a one-to-many relationship.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents a book written by an author.
# Each book is linked to one Author via a ForeignKey.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
