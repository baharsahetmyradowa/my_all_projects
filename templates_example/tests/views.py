from django.shortcuts import render

# Create your views here.

numbers=[]
for i in range(10):
    numbers.append(i)
def index(request):
    return render(request,"index.html",{
        "name":numbers
    })
food=["apple"]
def text(request):
    return render(request,"files/text.html",{
        "food":food 
    })

