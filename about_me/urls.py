from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list_view),
    path('book/<int:id>/', views.book_detail_view),
    path('book_list/', views.book_list_view, name='book_list'),
    path('tags/<str:tag_name>/', views.book_list_by_tag, name='book_list_by_tag'),
    path('create book/', views.create_book_view),
    path('book/<int:id>/delete/', views.drop_book_view),
    path('book/<int:id>/update/', views.edit_book_view),


]