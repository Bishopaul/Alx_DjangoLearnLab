from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, "relationship_app/library_detail.html", {"library": library})
