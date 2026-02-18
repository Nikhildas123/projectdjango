from django.shortcuts import render,redirect
from .models import book
from .forms import BookForm
# from django.http import HttpResponse


# def home(request):
#     return HttpResponse("Hello, Django!")

# def about(request):
#     return HttpResponse("hello,about!")


def home(request):
    data=["python","css","js","react","django"]
    return render(request,"home.html",{"a":data})
def about(request):
    data = {
        'name': 'Nikhil',
        'age': 21,
        'course': 'B.Sc Computer Science',
    }
    return render(request, 'about.html', data)
def contact(request):
    return render(request,"contact.html")

def viewbook(request):
    a=book.objects.all()
    return render(request,'viewbook.html',{"ab":a})
def addbook(request):
    a=BookForm(request.POST or None)
    if a.is_valid():
        a.save()
        return redirect('viewbook')
    return render(request,'addbook.html',{"abc":a})