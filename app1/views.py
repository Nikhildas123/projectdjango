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

def update_book(request,id):
    a=book.objects.get(id=id)
    b=BookForm(request.POST or None,instance=a)
    if b.is_valid():
        b.save()
        return redirect('viewbook')
    return render(request,"update_book.html",{"ab":b})   

def deletebook(request,id):
    a=book.objects.get(id=id)
    if request.method=='POST':
        a.delete()
        return redirect(viewbook)
    return render(request,'deletebook.html',{"abc":a})
