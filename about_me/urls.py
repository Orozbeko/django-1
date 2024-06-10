from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list_view),
    path('book/<int:id>/', views.book_detail_view),
    path('', views.book_list_view, name='book_list'),
]