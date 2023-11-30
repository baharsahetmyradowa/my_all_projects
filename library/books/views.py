from django.shortcuts import render
from books.models import Book
from django.http import Http404
# Create your views here.

def index(request):
    def_books=Book.objects.all()
    return render(request,"library/index.html",{
        "books": def_books,

    })
def book_detail(request,slug):
    try:
        book_detail=Book.objects.get(slug=slug)
       
    
    except:
        raise Http404()    
    return render(request,"library/book_detail.html",{
            "book_detail":book_detail
        })

