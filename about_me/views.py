from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from about_me.models import Book,Poster,Books


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



