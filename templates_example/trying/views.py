from django.shortcuts import render

# Create your views here.

fruits=['cherry','banana','strawberry','blueberry']

def index(request):
    return render(request,"index.html",{
        "fruit":fruits
    })