from django.shortcuts import render
from django.http import HttpResponse
from book.forms import CreateBookForm
from book.models import Book
from reader.models import Reader

# Create your views here.

def create_reader(request):
    if request.method == "POST":
        form = CreateBookForm(request.POST)
        if form.is_valid():
            reader_name = form.cleaned_data['name']
            reader_lastname = form.cleaned_data['lastname']
            reader = Reader.objects.create(name=reader_name, lastname=reader_lastname)
            reader.save()
            
            book = Book.objects.all()[len(Book.objects.a;;())-1]
            return HttpResponse("last edded book: " + book_name + ", Author: " + book_author)
    form = CreateReaderForm()
    return render(request, 'create_reader.html', {'form' : form})