from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo

def index(request):
    # content = {'message':"hello python"}
    books = BookInfo.objects.all()
    print(books)
    content = {"books":books}
    return render(request, "index.html", content)
