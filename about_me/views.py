from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from about_me.models import Book


def book_list_view(request):
    if request.method == 'GET':
        query = Book.objects.filter().order_by('-id')
        return render(
            request,
            template_name='blog/book_list.html',
            context={
                'book': query
            }
        )
    

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
        return render(
            request,
            template_name='blog/book_detail_.html',
            context={
                'book_id': book_id
            }
        )
    

        
             
             