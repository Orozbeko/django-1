from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BooklistView.as_view()),
    path('book/<int:id>/', views.BookDetailView.as_view()),
    path('book_list/', views.BookListByTagView, name='book_list'),
    path('tags/<str:tag_name>/', views.BookListTagView, name='book_list_by_tag'),
    path('create book/', views.CreateBookView.as_view()),
    path('book/<int:id>/delete/', views.BookDeleteView.as_view()),
    path('book/<int:id>/update/', views.EditBookView.as_view()),
    path('search/', views.SearchListView.as_view(), title='search'),
]