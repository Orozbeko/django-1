from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
<<<<<<< HEAD
from about_me.models import Book

=======
from random import randint
>>>>>>> 8c3c816d521b2de7586340e4f86263a3f8956763

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
    

<<<<<<< HEAD
        
             
             
=======
def random_numbers_view(request):
    if request.method == 'GET':
        return HttpResponse(random.randint(1, 100))
>>>>>>> 8c3c816d521b2de7586340e4f86263a3f8956763
