from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book_detail.html", {"book": book})

def create_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        description = request.POST["description"]
        published_date = request.POST.get("published_date")

        Book.objects.create(
            title=title,
            author=author,
            description=description,
            published_date=published_date
        )
        return redirect("book_list")

    return render(request, "create_book.html")

def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.description = request.POST["description"]
        book.published_date = request.POST.get("published_date")

        book.save()
        return redirect("book_detail", id=id)

    return render(request, "update_book.html", {"book": book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect("book_list")