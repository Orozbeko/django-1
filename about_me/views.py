from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from about_me.models import Book,Poster,Books,Tag
from django.views import generic
from . import forms


class SearchListView(generic.ListView):
    template_name = "blog/book_list.html"
    context_object_name = 'book'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get('pog')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pog'] = self.request.GET.get('pog')
        return context


class EditBookView(generic.UpdateView):
    template_name = 'blog/edit_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBookView, self).form_valid(form=form)


class BookDeleteView(generic.DeleteView):
    template_name = 'blog/confirm_delete.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Book, id=book_id)


class CreateBookView(generic.CreateView):
    template_name = 'blog/create_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)



class BooklistView(generic.ListView):
    template_name = "blog/book_list.html"
    context_object_name = "book"
    model = Book
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posters'] = Poster.objects.order_by('-id')
        context['books'] = Books.objects.order_by('-id')
        return context

class BookDetailView(generic.DetailView):
    template_name = 'blog/book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Book, id=book_id)


class BookListByTagView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        tag = get_object_or_404(Tag, name=tag_name)
        return tag.books.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_name = self.kwargs['tag_name']
        tag = get_object_or_404(Tag, name=tag_name)
        context['tag'] = tag
        return context

class BookListTagView(generic.ListView):
    model = Tag
    template_name = 'book_list.html'
    context_object_name = 'tag'
    slug_field = 'name'
    slug_url_kwarg = 'tag_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


