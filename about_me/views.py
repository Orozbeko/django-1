from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from about_me.models import Book,Poster,Books,Tag
from . import forms


def edit_book_view(request, id):
    book_id = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Book successfully updated!</h3>'
                                '<a href="books/">На список книг</a>')

    else:
        form = forms.BookForm(instance=book_id)
    return render(request, template_name='blog/edit_book.html',
                  context={
                      'form': form,
                      'book_id': book_id
                  })


def drop_book_view(request, id):
    book_id = get_object_or_404(Book, id=id)
    book_id.delete()
    return HttpResponse('Book deleted <a href="books/">На список книг</a>')


def create_book_view(request):
    if request.method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3> Book successfully created!</h3>'
                                '<a href="books/">На список книг</a>')
    else:
        form =forms.BookForm()
    return render(request, template_name='blog/create_book.html',
                  context={'form': forms})





def book_list_view(request):
    if request.method == 'GET':
        query = Book.objects.filter().order_by('-id')
        posters = Poster.objects.filter().order_by('-id')
        books = Books.objects.filter().order_by('-id')
        return render(
            request,
            template_name='blog/book_list.html',
            context={
                'book': query,
                'posters': posters,
                'books': books
            }
        )


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
        return render(
            request,
            template_name='blog/book_detail.html',
            context={
                'book_id': book_id
            }
        )

def book_list(request):
    age_category = request.GET.get('age_category')
    if age_category:
        books = Book.objects.filter(tags__name=age_category)
    else:
        books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books, 'age_category': age_category})

def book_list_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    books = tag.books.all()
    return render(request, 'book_list.html', {'tag': tag, 'books': books})


