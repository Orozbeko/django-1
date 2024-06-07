from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list_view),
    path('book/<int:id>/', views.book_detail_view),
    path('about/', views.about_me_views),
    path('myhobby/', views.hobby_view),
    path('datatime/', views.time_view),
    path('random_numbers/', views.random_numbers_view),
]