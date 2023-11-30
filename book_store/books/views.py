from django.shortcuts import render
from django.http import HttpResponse
from books.models import Boooks

# Create your views here.
def all_books(request):
    books=Boooks.objects.all()
    return render(request, "books/all_books.html",{
        "books":books
    })

def book_detail(request,slug):
    book_detail=get_object_or_404(Books,slug=slug)
    book_detail=Boooks.objects.get(pk=id)
    return render(request,"books/book_detail.html",{
        "book_detail":book_detail
    })    